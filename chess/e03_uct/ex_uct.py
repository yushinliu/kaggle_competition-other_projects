"""
Implement a chess player based on the python-chess library, which we put
into your repository. The player should use UCT to get the best move. Use
the ChessNode tree structure to build the tree and search in it.

The chess player has one local board on which moves can be simulated
without playing them on the official board:

    board.simulate_move(move)

To simulate all moves which correspond to one particular node in the tree
you can call:

    board.simulate_moves_from_node(node)

Since this local board is reused for all nodes, you have to reset it after
you simulated moves on it:

    board.reset_simulated_moves()


Some more examples of the use of python-chess:

To randomly choose a move from all legal moves you can do:

    random.choice([m for m in board.legal_moves])

This generates a list from all legal_moves (which is a generator object
and can only be iterated over) and than randomly chooses one of the entries.


You can check for a terminal state of a board with:

    board.is_game_over()

And for checkmate with

    board.is_checkmate()

Thus you can check who won with e.g.:

    if board.is_checkmate():
        if board.turn == player:
            pass  # checkmate and players turn -> opponent wins
        else:
            pass  # checkmate and opponents turn -> player wins
    elif board.is_game_over():
        pass  # draw


Make sure your implementation works for both
player == chess.WHITE and player == chess.BLACK
"""

from __future__ import division
import chess
import random
import math
from evaluation import evaluation


class ChessPlayer(object):
    """
    A chess player class that uses a Monte-Carlo tree search to get the
    next best move. The basic structure is already implemented for you,
    so that you don't have to care about pruning away parts of the tree
    and updating the root after each move.
    """
    def __init__(self, board, player):
        self.player = player
        self.board = board
        self.root = ChessNode(self.board, None, None)

    def inform_move(self, move):
        self.board.push(move)
        if move in self.root.untried_legal_moves:
            self.root = ChessNode(self.board, None, move)
        else:
            for child in self.root.children:
                if child.move == move:
                    self.root = child
                    self.root.parent = None
                    break

    def get_next_move(self):
        """
        Generates moves until a time limit is reached.
        The last move generated within the limit will be the move
        you officially play.
        """
        while True:
            # I M P L E M E N T   U C T   H E R E


            # yield what appears to be the best move after each iteration
            yield None


class ChessNode(object):
    """
    A chess tree structure. We already put all legal moves in the
    self.untried_legal_moves list. You have to take care of removing
    moves from that list by yourself, when expanding the tree! Also
    self.number_of_rollouts and self.sum_of_rewards is not automatically
    updated.
    """
    def __init__(self, board, parent, move):
        self.parent = parent
        self.move = move
        self.children = []
        self.number_of_rollouts = 0.
        self.sum_of_rewards = 0.

        board.simulate_moves_from_node(self)
        self.untried_legal_moves = [move for move in board.legal_moves]
        self.is_game_over = board.is_game_over()
        self.turn = board.turn
        board.reset_simulated_moves()

    def move_history(self):
        """
        Generator for the moves that lead to this node
        """
        if self.parent is not None:
            for move in self.parent.move_history():
                yield move
            if self.move is not None:
                yield self.move

    def add_child(self, node):
        self.children.append(node)

    def backup(self, player, reward):
        """
        Backup the current counts and rewards after a rollout
        :param player: The player you are (either chess.WHITE or chess.BLACK)
        :param reward: Reward earned in a rollout
        """



    def best_child(self, beta):
        """
        Return the best child of this node.

        :param beta: The constant beta from the UCB algorithm
        :return: A ChessNode
        """
        pass

    def tree_policy(self, board):
        """
        Return the most promising node to expand from this subtree.
        :param board: The players local board
        :return: A ChessNode
        """

        self = ChessNode(board, None, None)
        if board.is_checkmate():
            pass # noch zu implementiere
        if self.untried_legal_moves is not None:
            return expand(self.untried_legal_moves)
        else

    pass

    def expand(self, board):
        """
        Expand this node with a random child and return the child node
        :param board: The players local board
        :return: A ChessNode
        """
        """ab hier implementiert von Ziyong"""








    def default_policy(self, player, board):
        """
        Do a single rollout starting from this node and return a reward for the
        terminal state.

        If you recognize that a full rollout is too slow to get UCT running
        reasonably well, use the evaluation function in evaluation.py to cap
        the depth of the rollouts.

        If you are good at chess, you might as well write your own board-
        evaluation function.

        :param player: The player you are (either chess.WHITE or chess.BLACK)
        :param board: The players local board
        :return: reward
        """
        pass

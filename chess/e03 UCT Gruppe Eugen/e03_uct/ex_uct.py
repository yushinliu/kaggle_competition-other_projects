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
        pass

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
        float_score = 0
        test_move = None
        
        for mov in board.legal_moves:
            testnode = Chessnode(board, self, mov)
            float_score_tempt = evaluation.evaluation(testnode.board)
            self.children.append ([testnode, float_score_tempt])
            
            if float_score < float_score_temp:
                float_score = float_score_temp
                
                test_move = mov
                
        return test_move
        

    def expand(self, board):
        """
        Expand this node with a random child and return the child node
        :param board: The players local board
        :return: A ChessNode
        """
        try:
            rnd_move = random.choice([m for m in self.untried_legal_moves])
            return ChessNode(self.board, self, rnd_move)
        except:
            return self

    def default_policy(self, player, board):
        """
        Do a single rollout starting from this node and return a reward for the
        terminal state.

        If you recognize that a full rollout is too slow to get UCT running
        reasonably well, use the evaluation function in evaluation.py to cap
        the depth of the rollouts.

        If you are good at chess, you might as well write eyour own board-
        evaluation function.

        :param player: The player you are (either chess.WHITE or chess.BLACK)
        :param board: The players local board
        :return: reward
        """
        node = self #???
        # random moves expandieren
        for i in range(1, 50):
            if i >= 5:
                # evaluate via fnktion
                flt_evalu = evaluation.evaluation(node.board)
                #return flt_evalu
                #if flt_evalu == 0:
                    #return 0
                if node.board.turn == chess.BLACK:#flt_evalu > 0:
                    if flt_evalu > 0:
                        return 1
                    else:
                        return -1
                elif node.board.turn == chess.WHITE:
                    if flt_evalu < 0:
                        return 1
                    else:
                        return -1
                else:
                    return 0

            node = node.expand()
            if node.board.is_checkmate():
                if node.board.turn == chess.BLACK:
                    return -1.  # checkmate and blacks turn -> white wins
                elif node.board.turn == chess.WHITE:
                    return 1.  # checkmate and whites turn -> black wins
            elif node.board.is_game_over():
                return 0.  # draw
        return 0    # sollte nicht vorkommen, wenn doch, keine info gegeben


def uct_search(root, secs, player):
    start = time.time()
    fringe = [m for m in root.board.legal_moves]
    ndict =  []
    #print fringe
    counter = 0
    nodebest = fringe[0]#ChessNode(root.board, root, fringe[0])
    valbest = -10
    while True:
        # I M P L E M E N T   U C T   H E R E
        # Don't write the outer loop again. The for loop
        # is supposed to do that for you
        if counter >=  len(fringe):
            break
        nodeval = (ChessNode(root.board, root, fringe[counter])).default_policy()#tree_policy()
        if valbest <= nodeval:
            nodebest = fringe[counter]
            ndict.append(fringe[counter])
            valbest = nodeval
        counter = counter + 1
        if time.time() - start > secs:
            print("Zeit ueberschritten!")
            break

    return random.choice(ndict)#nodebest  # return the best nodemove    

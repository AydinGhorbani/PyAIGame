# Main Author: Aydin Ghorbani
# Main Reviewer: Professor Adarsh Sehgal

def copy_board(board):
    current_board = []
    height = len(board)
    for i in range(height):
        current_board.append(board[i].copy())
    return current_board

def evaluate_board(board, player):
    borad_pos, borad_neg = False, False
    for row in board:
        for cell in row:
            borad_pos |= cell > 0
            borad_neg |= cell < 0
            if borad_pos and borad_neg:
                return 0
            
    if borad_pos and borad_neg:
        return 0  # Game is ongoing
    if (player == 1 and not borad_neg) or (player == -1 and not borad_pos):
        return 1  # Current player wins
    return -1  # Opponent wins

    
class GameTree:
    class Node:
        def __init__(self, board, depth, player, tree_height=4):
            self.board = copy_board(board)
            self.depth = depth
            self.height = tree_height
            self.player = player
            self.children = []
            self.score = 0 

    def __init__(self, board, player, tree_height=4):
        self.player = player
        self.board = copy_board(board)
        self.root_node = self.Node(board, 0, player, tree_height)
        self.minimax(self.root_node)

    def minimax(self, node):
        if node.depth == node.height - 1:
            node.score = evaluate_board(self.board, self.player)
        else:
            for child_node in node.children:
                self.minimax(child_node)
                
         # decide the  comparison based on node depth (minimizing or maximizing)
            if node.children:
                best_score = None
                is_minimizing = (node.depth % 2) == 0 
                # the conditional check for minimizing
                for child in node.children:
                    if child.score is not None and (best_score is None or 
                        (child.score < best_score if is_minimizing else child.score > best_score)):
                        best_score = child.score
                node.score = best_score

    def get_move(self):
        next_move, best_score = None, None
        for child in self.root_node.children:
            if child.score is not None and (best_score is None or child.score > best_score):
                next_move, best_score = child.move, child.score
        return next_move or (0, 1)

    def clear_board(board):
        for row in range(len(board)):
            for col in range(len(board[row])):
                board[row][col] = 0

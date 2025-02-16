from a2_partb import GameTree

class PlayerOne:
    def __init__(self, name="P1 Bot", difficulty=1):
        self.name = name
        self.difficulty = difficulty  # difficulty affects the depth of the game tree

    def get_name(self):
        return self.name

    def get_play(self, board):
        # create a game tree with the specified difficulty level (depth)
        tree = GameTree(board, 1, depth=self.difficulty)
        (row, col) = tree.get_move()
        return (row, col)

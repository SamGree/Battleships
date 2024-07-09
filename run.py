from random import randint


scores = {'computer': 0, 'player': 0}
"""
Initializes a dictionary to keep track of the scores
for the computer and the player, both starting at 0.
"""
class Board:
    """
    Defines a class Board which will represent the game board.
    """
    def __init__(self, size, num_ships, name, type):
        self.size = size
        self.board =[[" " for _ in range(size)] for _ in range(size)]
        self.num_ships = num_ships
        self.name = name
        self.type = type
        self.guesses = []
        self.ships = []
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

def print(self, hide_ships = False) :
        print(f"{self.name}'s board:")   
        print("   " + "   ".join(str(i) for i in range(self.size)))
        for idx, row in enumerate(self.board):
            print("  " + "---|" * self.size)
            if hide_ships:
                row_to_print = [" " if cell == "@" else cell for cell in row]
                print(str(idx) + " " + "  |".join(row_to_print) + "  |")
            else:
                print(str(idx) + " " + "  |".join(row) + "  |")    
        print("  " + "---|" * self.size)      


def guess(self, x, y):
        """
        Process a guess at coordinates (x, y).
        This method checks if the guessed coordinates hit a ship.
        It updates the board and the guesses list accordingly.
        """

        self.guesses.append((x, y))      
        if (x, y) in self.ships:
            self.board[x][y] = '*'
            return "Hit"
        else:
            self.board[x][y] = 'X'     
            return "Miss"

def add_ship(self, x, y):

        """
        Adds a ship at the specified coordinates (x, y)
        if the maximum number of ships has not been reached.
        For player boards, marks the ship's position.
        """
        if len(self.ships) >= self.num_ships:
            print("Error: you cannot add more ships!")
        else:
            self.ships.append((x, y))
            if self.type == "player":
                self.board[x][y] = "~"  

def random_point(size):
        """
        Returns a random point on the board between 0 and size
        """
        return randint(0, size - 1)
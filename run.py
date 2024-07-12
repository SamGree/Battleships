from random import randint
from colorama import Fore, Style, init

# Initialize colorama
init(autoreset=True)

# Initialize scores for both the computer and the player
scores = {'computer': 0, 'player': 0}


class Board:
    """
    A class to represent a board in a game
    """

    def __init__(self, size, num_ships, name, type):
        self.size = size
        self.board = [[" " for _ in range(size)] for _ in range(size)]
        self.num_ships = num_ships
        self.name = name
        self.type = type
        self.guesses = []
        self.ships = []

    def print(self, hide_ships=False):
        print(f"{self.name}'s Board:")
        print("   " + "   ".join(str(i) for i in range(self.size)))
        for idx, row in enumerate(self.board):
            print("  " + "---|" * self.size)
            if hide_ships:
                row_to_print = [" " if cell == "@" else cell for cell in row]
                print(str(idx) + " " + "  |".join(row_to_print) + "  |")
            else:
                row_to_print = [Fore.RED + cell + Style.RESET_ALL if cell == '*'
                else cell
                for cell in row]
                print(str(idx) + " " + "  |".join(row) + "  |")
        print("  " + "---|" * self.size)

    def guess(self, x, y):
        self.guesses.append((x, y))
        if (x, y) in self.ships:
            self.board[x][y] = Fore.LIGHTRED_EX + '*' + Style.RESET_ALL
            return "Hit"
        else:
            self.board[x][y] = Fore.LIGHTBLUE_EX + 'X' + Style.RESET_ALL
            return "Miss"

    def add_ship(self, x, y):
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


def valid_coordinates(x, y, size):
    """
    Check if the given coordinates are within the board limits
    """
    return 0 <= x < size and 0 <= y < size


def populate_board(board):
    """
    Populate the board with ships at random locations
    """
    while len(board.ships) < board.num_ships:
        x = random_point(board.size)
        y = random_point(board.size)
        if (x, y) not in board.ships:
            board.add_ship(x, y)


def make_guess(board):
    """
    Make a guess for the player, ensuring it's a valid and new guess
    """
    while True:
        try:
            x = int(input("Guess Row: "))
            y = int(input("Guess Col: "))
            valid_coords = valid_coordinates(x, y, board.size)
            new_guess = (x, y) not in board.guesses
            if valid_coords and new_guess:
                return x, y
            else:
                print("Invalid or repeated guess. Try again.")
        except ValueError:
            print("Invalid input. Please enter numbers only.")


def play_game(player_board, computer_board, max_shots):
    """
    Main game loop for playing the game
    """
    print("Let's start the game!")
    turn = "player"
    player_shots = 0
    computer_shots = 0

    while player_shots < max_shots and computer_shots < max_shots:
        if turn == "player":
            print("\nPlayer's turn!")
            player_board.print()
            computer_board.print(hide_ships=True)
            x, y = make_guess(computer_board)
            result = computer_board.guess(x, y)
            print(f"Player guessed ({x}, {y}) - {result}")
            if result == "Hit":
                scores['player'] += 1
            player_shots += 1
            turn = "computer"
        else:
            print("\nComputer's turn!")
            while True:
                x = random_point(player_board.size)
                y = random_point(player_board.size)
                if (x, y) not in player_board.guesses:
                    break
            result = player_board.guess(x, y)
            print(f"Computer guessed ({x}, {y}) - {result}")
            if result == "Hit":
                scores['computer'] += 1
            computer_shots += 1
            turn = "player"
        if scores['player'] == player_board.num_ships:
            print("Congratulations! You have won the game!")
            break
        elif scores['computer'] == player_board.num_ships:
            print("Oh no! The computer has won the game!")
            break

    if player_shots >= max_shots or computer_shots >= max_shots:
        print("Game over! Maximum number of shots reached.")
        print("\nFinal scores:")
        print(f"Player: {scores['player']}")
        print(f"Computer: {scores['computer']}")


def new_game():
    """
    Start a new game, set the board size and number of ships,
    reset the scores, and initialize the boards.
    """
    size = 5
    num_ships = 5
    max_shots = 12  # Maximum number of shots each player can take
    scores['computer'] = 0
    scores['player'] = 0

    print("-" * 35)
    print("-Welcome to Battleships: Player vs Computer!")
    print("-Game Setup: Board size is 5x5 with 5 ships.")
    print("-Coordinates: Top left corner is at (0, 0).")
    print("-Shooting Rules: Enter coordinates between 0 and 4.")
    print(f"-Objective: Sink all ships with in {max_shots} shots to win!")
    print("-" * 35)
    player_name = input("What is your name? \n")
    print("-" * 35)

    computer_board = Board(size, num_ships, "Computer", type="computer")
    player_board = Board(size, num_ships, player_name, type="player")
    # Start computer and player boards with specified size and number of ships

    populate_board(computer_board)
    populate_board(player_board)
    # Populate the computer and player boards with ships

    play_game(player_board, computer_board, max_shots)
    # Start and run the game loop with the player
    # and computer boards and a maximum number of shots

# Start a new game


new_game()

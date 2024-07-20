from random import randint
from colorama import Fore, Style, init
import os


# Initialize colorama
init(autoreset=True)

# Initialize scores for both the computer and the player
scores = {'computer': 0, 'player': 0}

class Board:
    def __init__(self, size, num_ships, name, type):
        self.size = size
        self.board = [[" " for _ in range(size)] for _ in range(size)]
        self.num_ships = num_ships
        self.name = name
        self.type = type
        self.guesses = []
        self.ships = []

    def print_board(self, hide_ships=False):
        print(f"{self.name}'s Board:")
        print("   " + "   ".join(str(i) for i in range(self.size)))
        for idx, row in enumerate(self.board):
            print("  " + "---|" * self.size)
            if hide_ships:
                row_to_print = [" " if cell == "@" else cell for cell in row]
                print(str(idx) + " " + "  |".join(row_to_print) + "  |")
            else:
                row_to_print = [Fore.RED + cell + Style.RESET_ALL if cell == '*' else cell for cell in row]
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
    return randint(0, size - 1)

def valid_coordinates(x, y, size):
    return 0 <= x < size and 0 <= y < size

def populate_board(board):
    while len(board.ships) < board.num_ships:
        x = random_point(board.size)
        y = random_point(board.size)
        if (x, y) not in board.ships:
            board.add_ship(x, y)

def make_guess(board):
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
            print("Invalid input. Please enter numbers only 0 to 4.")

def play_game(player_board, computer_board, max_shots):
    print("Let's start the game!")
    turn = "player"
    player_shots = 0
    computer_shots = 0

    while player_shots < max_shots and computer_shots < max_shots:
        if turn == "player":
            clear_screen()
            print("\n Your turn!")
            computer_board.print_board(hide_ships=True)
            print(f"You have {max_shots - player_shots} shots left.")
            x, y = make_guess(computer_board)
            result = computer_board.guess(x, y)
            print(f"You guessed ({x}, {y}) - {result}")
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
        print(f"Your scores: {scores['player']}")
        print(f"Computer scores: {scores['computer']}")

        if scores['player'] > scores['computer']:
            print(f"Congratulations {player_board.name}! You won!")
        elif scores['computer'] > scores['player']:
            print(f"Computer wins! Better luck next time, {player_board.name}!")
        else:
            print("It's a tie!")


def clear_screen():
    os.system("cls" if os.name == "nt" else "clear")

def new_game():
    size = 5
    num_ships = 5
    max_shots = 12
    scores['computer'] = 0
    scores['player'] = 0
    
    print(Fore.YELLOW + "-Instructions." + Style.RESET_ALL)
    print("-" * 35)
    print(Fore.LIGHTGREEN_EX + "-Welcome to Battleships: Player vs Computer!" + Style.RESET_ALL)
    print("-Game Setup: Board size is 5x5 with 5 ships.")
    print("-Coordinates: Top left corner is at (0, 0).")
    print("-Shooting Rules: Enter coordinates between 0 and 4.")
    print(f"-Objective: Sink all ships within {max_shots} shots to win!")
    print("-" * 35)

    while True:
        option = input("-Type 'e' to exit 'c' to continue: ").lower()
        if option == 'e':
            print("Goodbye")
            return False
        elif option == 'c':
            break
        else:
            print("Invalid. Please type 'e' to exit or 'c' to continue.")    

    while True:
        player_name = input("-Your name Please?\n ")
        if player_name.isalpha() and len(player_name) <= 10:
            break
        else:
            print("-Invalid input.")

    print("-" * 35)
    computer_board = Board(size, num_ships, "Computer", type="computer")
    player_board = Board(size, num_ships, player_name, type="player")
    populate_board(computer_board)
    populate_board(player_board)

    play_game(player_board, computer_board, max_shots)
    return True

def main():
    while new_game():
        while True:
            play_again = input("Do you want to play again? (y / n): ").lower()
            if play_again in ["y", "n"]:
                break
            print("Invalid input. Please type 'y' to play again or 'n' to exit.")
        if play_again == "n":
            print("Thank you for playing! Goodbye.")
            break
        clear_screen()

if __name__ == "__main__":
    main()

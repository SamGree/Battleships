# Battleships Game
  - The Battleships game is a turn-based game where the player competes against the computer. The game consists of a grid (board) where ships are placed. Players take turns guessing the locations of the opponent's ships, trying to "hit" and sink them.


## Table of Contents
- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Game Rules](#game-rules)
- [Design Components](#design-components)
- [Class: Board](#class-board)
- [Attributes](#attributes)
- [Methods](#methods)
- [Contributing](#contributing)
- [License](#license)
- [Acknowledgements](#acknowledgements)

## Features
- Play the classic Battleships game against the computer.
- 5x5 board with 5 ships.
- Simple and intuitive interface.
- Color-coded feedback for hits and misses.

## Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/SamGree/Battleships.git
    cd battleships
    ```

2. Install the required packages:
    ```bash
    pip3 frezze --local > requirements.txt
    ```
## Usage 
    - To start the game, just type your player name

## Game Rules
  - Board Size: The game is played on a 5x5 grid.
  - Ships: Each player has 5 ships.
  - Shots: Enter the row and column to make a shot (coordinates between 0 and 4).
  - Winning: Sink all the opponent's ships within 12 shots to win the game.

## Design Components
 
  1- Class: Board. 
  2- Functions for Game Logic.
  3- Main Game Loop.
  4- User Interface.

## Class: Board  
The Board class represents the game board for each player.
#### Attributes
 - __size:__ Size of the board (e.g., 5x5)
 - __board:__ A 2D list representing the board grid.
 - __num_ships:__ Number of ships on the board.
 - __name:__ Name of the board owner (e.g., "Player" or "Computer").
 - __type:__ Type of the board owner (e.g., "player" or "computer").
 - __guesses:__ List of guesses made.
 - __ships0__: List of ship locations.
#### Methods
 - __init__: Initializes the board with the given size and number of ships.
 - __print:__ Prints the board to the termenal.
 - __guess:__ Handles a guess made on the board.
 - __add_ship__: Adds a ship to the board.
 
 #### Functions for Game Logic
  - random_point(size): Returns a random point on the board.
  - valid_coordinates(x, y, size): Checks if the given coordinates are within the board limits.
  - populate_board(board): Populates the board with ships at random locations.
  - make_guess(board): Prompts the player to make a guess, ensuring it's valid and new.
  - play_game(player_board, computer_board, max_shots): Main game loop for playing the game.
  - new_game(): Starts a new game, setting up the boards and initializing scores.






## Contributing
- This project is licensed under the MIT License.

## Acknowledgements
 - colorama for terminal color formatting.



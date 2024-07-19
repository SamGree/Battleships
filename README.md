# *Battleships Game*

  - The Battleships game is a turn-based game where the player competes against the computer. The game consists of a grid (board) where ships are placed. Players take turns guessing the locations of the opponent's ships, trying to "hit" and sink them.
  > - Link to the battleships game 
  > <https://battleships-sam-f594730cad42.herokuapp.com/>

  - ![Tux, the Linux mascot](/readme.images/ami.responsive.ships.png) 
  

## **Table of Contents**
- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Game Rules](#game-rules)
- [Design Components](#design-components)
- [Class: Board](#class-board)
- [Functions for Game Logic](#functions-for-game-logic)
- [Flowchart](#flowchart)
- [How to play](#how-to-play)
- [Testing](#testing)
- [Credits](#credits)
- [Acknowledgements](#acknowledgements)



## **Features**
- Play the classic Battleships game against the computer.
- 5x5 board with 5 ships.
- Simple and intuitive interface.
- Color-coded feedback for hits and misses.

## **Installation**

1. Clone the repository:
    
    - git clone <https://github.com/SamGree/Battleships>   

2. Install the required packages:
    - pip3 freeze  -- local > requirements.txt
    
    

## **Usage** 
    - To start the game, just type your name.
  
## **Game Rules**
  - Board Size: The game is played on a 5x5 grid.
  - Ships: Each player has 5 ships.
  - Shots: Enter the row and column to make a shot (coordinates between 0 and 4).
  - Winning: Sink all the opponent's ships within 12 shots to win the game.
   - ![Tux, the Linux mascot](/readme.images/run.program.png)

## **Design Components**
 
  1. Class: Board. 
  2. Functions for Game Logic.
  3. Main Game Loop.
  4. User Interface.

> ## **Class: Board**  
> - The Board class represents the game board for each player.
> ### Attributes
> - **size:** Size of the board (e.g., 5x5)
> - **board:** A 2D list representing the board grid.
> - **num_ships:** Number of ships on the board.
> - **name:** Name of the board owner (e.g., "Player" or "Computer").
> - **type:** Type of the board owner (e.g., "player" or "computer").
> - **guesses:** List of guesses made.
> - **ships:** List of ship locations.
>### Methods
> - __init__: Initializes the board with the given size and number of ships.
> - **print:** Prints the board to the termenal.
> - **guess:** Handles a guess made on the board.
> - **add_ship:** Adds a ship to the board.
 
> ## **Functions for Game Logic**
>  - random_point(size): Returns a random point on the board.
>  - valid_coordinates(x, y, size): Checks if the given coordinates are within the board limits.
> - populate_board(board): Populates the board with ships at random locations.
>  - make_guess(board): Prompts the player to make a guess, ensuring it's valid and new.
> - play_game(player_board, computer_board, max_shots): Main game loop for playing the game.
> - new_game(): Starts a new game, setting up the boards and initializing scores.
> ### Main Game Loop
> - The main game loop will handle the turns between the player and the computer, updating the game state after each guess. It will continue until one player sinks all the opponent's ships or the maximum number of shots is reached.

> ## **User Interface.**
> - The user interface will be text-based, using print statements to display the game state and prompts for player input. The colorama library can be used to enhance the display with colors.
> - ![Tux, the Linux mascot](/readme.images/requirements.png)

## **Flowchart**
- ![Tux, the Linux mascot](/readme.images/flowchart.png)

> ## **How to play**
> - In this game you manually type your name to start the game. then board grids will be displayed for both first Computer grid then second player grid. Row will be first to write between 0  to 4, then col will appear this also 0 to 4 .
> - ![Tux, the Linux mascot](/readme.images/type.name.png)
> - ![Tux, the Linux mascot](/readme.images/player.board.png)
> - ![Tux, the Linux mascot](/readme.images/computer.borad.png)
---
- ( ~ ) This symbol is your ships which computer locate them automatically.
- ( X )  in blue its mean you miss.
- ( * ) in red its mean you hit the target.
- ![Tux, the Linux mascot](/readme.images/miss.hit.png)
---
---
- If the player enters a letter instead of a number, an error message will be displayed.
- ![Tux, the Linux mascot](/readme.images/string.enter.png)
---
---
- If the player enters a number outside the valid range or repeats a previously guessed number, an error message will be displayed.
- ![Tux, the Linux mascot](/readme.images/repeated.guess.png)
- ![Tux, the Linux mascot](/readme.images/number.outof.range.png)
---
---
- If player make 12 shots and not sink all ships, game will end.
- ![Tux, the Linux mascot](/readme.images/max.shots.png)
> - If player won the game.
> ![Tux, the Linux mascot](/readme.images/player.won.png)
---
> - if computer won the game. 
> ![Tux, the Linux mascot](/readme.images/computer.won.png)
---
- if you want to start the game again, simply press RUN PROGRAM.
- ![Tux, the Linux mascot](/readme.images/run,program.png)

## Deployment
 -  Deploy this project to Heroku, I did the following steps
  1. Push all codes to Github.
  2. Go to Heroku page and login.
  3. Create new app.
  4. App name (battleships) and choose Europe for region.
  5. create app.
  6. Click GitHub, connect to Github.
  7. Go to the settings tab.
  8.  Config vars
  9.  KEY is (PORT) and VALUE is (8000) then click ADD. 
  10. Add buildpack.
  11. Select Python, then save changes.
  12. Select Nodejs, then save changes.
  13. Ensure that Heroku/Python is at the top of the list, followed by Heroku/Nodejs
 14. Go to the deploy tab and Select github.
 15. confirm what I want to connect to github.
 16. Now we can search for github repository name. 
  and  Scroll down to Manual Deploy and select deploy branch finally click connect.

> ### Testing
> - All of the code within this program was tested using Code Institute's PEP8.
> ![Tux, the Linux mascot](/readme.images/pep8.png)

## Credits
 - This video help me to understand basic python <https://www.youtube.com/watch?v=XKHEtdqhLK8>
 - The main structure of this game coming from code institute including the codes.<https://learn.codeinstitute.net/courses/course-v1:CodeInstitute+PE_PAGPPF+2021_Q2/courseware/b3378fc1159e43e3b70916fdefdfae51/605f34e006594dc4ae19f5e60ec75e2e/>

 

## **Acknowledgements**
 - Special thanks to my mentor **Luke Buchanan** for the feedback as always. 
 -  Thanks to **Tutor Assistance** for their constant support and guidance whenever I needed help.



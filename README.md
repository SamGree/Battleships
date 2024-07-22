# *Battleships Game*

  - The Battleships game is a turn-based game where the player competes against the computer. The game consists of a grid (board) where ships are placed. Players take turns guessing the locations of the opponent's ships, trying to "hit" and sink them.
  > - Link to the battleships game 
  > <https://battleships-sam-f594730cad42.herokuapp.com/>

  - ![Tux, the Linux mascot](/readme.images/ami.responsive.battleship.png) 
  

## **Table of Contents**
- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Game Rules](#game-rules)
- [How to play](#how-to-play)
- [Design](#design)
- [Testing](#testing)
- [Credits](#credits)
- [Acknowledgements](#acknowledgements)



## **Features**
- Classic Battleships game: Player against the computer.
- Board Setup: 5x5 board with 5 ships.
- Simple and intuitive interface.
- Color-coded feedback for hits and misses.

## **Installation**

1. Clone the repository:
    
    - git clone <https://github.com/SamGree/Battleships>   

2. Install the required packages:
    - pip3 freeze  -- local > requirements.txt
    
    

## **Usage** 
    - You have to type - c -to continue then type player name to start the game, or - e - to exit.
  
## **Game Rules**
  - Board Size: The game is played on a 5x5 grid.
  - Ships: Each player has 5 ships.
  - Shots: Enter the row and column to make a shot (coordinates between 0 and 4).
  - Winning: Sink all the opponent's ships within 12 shots to win the game.
  - Type ( e ) to exit or ( c ) to start the game.
  > - ![Tux, the Linux mascot](/readme.images/new.instruction.png)

> ## **How to play**
> - Follow the instructions on-screen to start the game. then computer  board grid will be displayed on screen with hidden ships. Row will be first to write between 0  to 4, then col will be next to write between 0 to 4 .
> - ![Tux, the Linux mascot](/readme.images/computer.board.png)
---
- ( X )  in blue its mean you miss.
- ( * ) in red its mean you hit the target.
- ![Tux, the Linux mascot](/readme.images/redhit.bluemiss.png)


- If the player enters a letter instead of a number, an error message will be displayed.
- ![Tux, the Linux mascot](/readme.images/enter.no.only.png)
---
- If the player enters a number outside the valid range or repeats a previously guessed number, an error message will be displayed.
- ![Tux, the Linux mascot](/readme.images/repeat.guess.png)
- ![Tux, the Linux mascot](/readme.images/out.of.range.png)

---
- 12 shots and not sink all ships, game will end, The winner is the one got high scores
- ![Tux, the Linux mascot](/readme.images/reachmax.shot.png)
--- 
> - if scores will be equal for both player and computer the message will - It's a tie! -
---
- if you want to start the game again, enter y to start or n to end the game .
- ![Tux, the Linux mascot](/readme.images/play.again.png)

> ## **User Interface.**
> - When you start the game by running python run.py, you will see a welcome message and instructions about the game setup, including board size, ship count, and shooting rules.
> - ![Tux, the Linux mascot](/readme.images/requirements.png)

## **Design**
### Game Board:
- Class: Board
- Role: Manages the board, ship placement, and guesses. Includes methods to print the board, add ships, handle guesses, and validate coordinates.
### Game Logic:
- Flow: Alternates turns between the player and computer. The game ends when the shot limit is reached or all ships are sunk.
### Key Functions:
- new_game(): Initializes the game and shows instructions.
- play_game(): Runs the game loop with turn-taking and scoring.
- make_guess(), populate_board(), clear_screen(): Support functions for game operations.

### Design Choices

- **Modular Design:** Organized into classes and functions for clear separation and reusability. The **Board** class manages board operations, while game logic and UI are separate.
- **Error Handling:** Includes input validation and error messages for a better user experience.
- **Random Choice:** Computer moves are randomized using random_point() for unpredictable gameplay.
- **Text-Based Interface:** Simple implementation with colorama for color enhancements.
#### **Flowchart**
- ![Tux, the Linux mascot](/readme.images/flowchart2.png)
## **import**
- os: used for adding a clear() function
- import platform: used to perform OS-specific tasks, such as clearing the console screen.


## Deployment
 - All code from Gitpod was pushed to GitHub using the following steps:
   1. git add .
   2. git commit -m "Commit message"
   3. git push

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
> ![Tux, the Linux mascot](/readme.images/pep8.second.png)

> ## Bugs
 - Resolved Bugs
  - I missed capitalize (Style) in the print statement to color the header.It solved

     - ![Tux, the Linux mascot](/readme.images/s.should.be.capital.png)
  - I found extra dot at the end of the input option. It solved.

     - ![Tux, the Linux mascot](/readme.images/bug.extra.png)
- AttributeError: "str" object has no attribute "name".Then I ensure 
  that the class is defined correctly and the name attribute is properly assigned in the __init__ method. it solved.

     - ![Tux, the Linux mascot](/readme.images/bugs.python.png)
- name: error "randint" is not defined, solved by typing correct name.  
     - ![Tux, the Linux mascot](/readme.images/bug.randint.png)

- This error appear when I forgot to import the platform in the top of the file. It solved.
     - ![Tux, the Linux mascot](/readme.images/platform.forgot.png)
- Indentation errors - Received indentation errors e.g "line code too long, over-indented and trailing whitespace" Fixed the indentation by ensuring all code lines in the functions were correctly aligned.
     - ![Tux, the Linux mascot](/readme.images/indentation.png)   



## Credits
 - This video help me to understand basic of python <https://www.youtube.com/watch?v=XKHEtdqhLK8>
 - The main structure of this game coming from code institute. I used Code Institute’s code for my Battleships project to leverage their reliable solutions and best practices. This foundation provided proven techniques and efficient problem-solving. I then integrated my own code to customize and complete the project, ensuring it met specific requirements and aligned with Python programming goals.".<https://learn.codeinstitute.net/courses/course-v1:CodeInstitute+PE_PAGPPF+2021_Q2/courseware/b3378fc1159e43e3b70916fdefdfae51/605f34e006594dc4ae19f5e60ec75e2e/>
 - Those two websites gave me ideas on how to Building the gameboard.
 - <https://teamtreehouse.com/community/dont-know-how-to-start-python-project-2-battleship>
 - <https://stackoverflow.com/questions/53446425/creating-a-row-of-numbers-letters-in-my-python-battleship-game>

 

## **Acknowledgements**
 - Special thanks to my mentor **Luke Buchanan** for the feedback as always. 
 -  Thanks to **Tutor Assistance** for their constant support and guidance whenever I needed help.
 



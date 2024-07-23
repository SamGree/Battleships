# *Battleships Game*

  - Creating a Battleships game was a chance to combine my love for strategy and programming. I wanted to design a game that’s simple yet engaging, where players can test their tactical skills. It’s also a fun way to practice coding and game design, making it an enjoyable project from both a technical and creative perspective. Thanks to code institute for this chance. Plus I use to play with my son when he was little.
  > - Link to the battleships game 
  > <https://battleships-sam-f594730cad42.herokuapp.com/>

  ![Tux, the Linux mascot](/readme.images/ami.responsive.png) 
  

## **Table of Contents**
- [Design](#design)
- [Design Choices](#design-choices)
- [Features](#features)
- [Installation](#installation)
- [User Interface](#user-interface)
- [Usage](#usage)
- [Game Rules](#game-rules)
- [How To Play](#how-to-play)
- [Deployment](#deployment)
- [Testing](#testing)
- [Bugs](#bugs)
- [Credits](#credits)
- [Acknowledgements](#acknowledgements)

## Design
### Game Board:
- Class: Board
- Role: Manages the board, ship placement, and guesses. Includes methods to print the board, add ships, handle guesses, and validate coordinates.
### Game Logic:
- Flow: Alternates turns between the player and computer. The game ends when the shot limit is reached or all ships are sunk.
### Key Functions:
- new_game(): Initializes the game and shows instructions.
- play_game(): Runs the game loop with turn-taking and scoring.
- make_guess(), populate_board(), clear_screen(): Support functions for game operations.

## Design Choices

- **Modular Design:** Organized into classes and functions for clear separation and reusability. The **Board** class manages board operations, while game logic and UI are separate.
- **Error Handling:** Includes input validation and error messages for a better user experience.
- **Random Choice:** Computer moves are randomized using random_point() for unpredictable gameplay.
- **Text-Based Interface:** Simple implementation with colorama for color enhancements.
#### **Flowchart**
![Tux, the Linux mascot](/readme.images/flowchart.final.png)

## Features
- Classic Battleships game: Player against the computer.
- Board Setup: 5x5 board with 5 ships.
- Simple and intuitive interface.
- Color-coded feedback for hits and misses.

## Installation

1. Clone the repository:
    
    - git clone <https://github.com/SamGree/Battleships>   

2. Install the required packages:
    - pip3 freeze  -- local > requirements.txt
     ![Tux, the Linux mascot](/readme.images/requirements.png)

> ## User Interface
> - When you start the game by running python run.py, you will see a welcome message and instructions about the game setup, including board size, ship count, and shooting rules.
    
    

## Usage
    - You have to type - c -to continue then type player name to start the game, or - e - to exit.
  
## Game Rules
  - Board Size: The game is played on a 5x5 grid.
  - Ships: Each player has 5 ships.
  - Shots: Enter the row and column to make a shot (coordinates between 0 and 4).
  - Winning: Sink all the opponent's ships within 12 shots to win the game.
  - Type ( e ) to exit or ( c ) to start the game.
  - As a player to enter your name to start the game: your input must be ***10 characters or fewer*** .
   ![Tux, the Linux mascot](/readme.images/new.instruction.png)

> ## How to play
> - Follow the instructions on-screen to start the game. Your input for name must be ***10 characters or fewer*** .Then computer  board grid will be displayed on screen with hidden ships. Row will be first to write between 0  to 4, then col will be next to write between 0 to 4 .
![Tux, the Linux mascot](/readme.images/enter.name.png)
---
- ( X )  in blue its mean you miss.
- ( * ) in red its mean you hit the target.
![Tux, the Linux mascot](/readme.images/row.col.red.png)


- If the player enter a letter instead of a number, an error message will be displayed.
![Tux, the Linux mascot](/readme.images/letter.insted.nu.png)
---
- If the player enters a number outside the valid range or repeats a previously guessed number, an error message will be displayed.
![Tux, the Linux mascot](/readme.images/not.inrang.png)

---
- If 12 shots and not sink all ships, game will end, The winner is the one who get the high scores
![Tux, the Linux mascot](/readme.images/i.won.png)
--- 
> - If scores will be equal for both player and computer the message will - It's a tie!
![Tux, the Linux mascot](/readme.images/tie.last.png)
---
- If you want to start the game again, enter y to start or n to end the game . and second option in RUN PROGRAM.
![Tux, the Linux mascot](/readme.images/two.option.png)



## **import**
- os: used for adding a clear() function
- import platform: used to perform OS-specific tasks, such as clearing the console screen.


## Deployment

 - **All code from Gitpod was pushed to GitHub using the following steps:**
 1. git add .
 2. git commit -m "Commit message"
 3. git push

 -  **Deploy this project to Heroku, I did the following steps:**
   1. Push all codes to Github.
   2. Go to Heroku page and login.
   3. Create new app.
   4. App name (battleships) and choose Europe for region.
   5. Create app.
   6. Click GitHub, connect to Github.
   7. Go to the settings tab.
   8.  Config vars
   9.  KEY is (PORT) and VALUE is (8000) then click ADD. 
   10. Add buildpack.
   11. Select Python, then save changes.
   12. Select Nodejs, then save changes.
   13. Ensure that Heroku/Python is at the top of the list, followed by Heroku/Nodejs
   14. Go to the deploy tab and Select github.
   15. Confirm what I want to connect to github.
   16. Now we can search for github repository name. 
  and  Scroll down to Manual Deploy and select deploy branch finally click connect.

> ## Testing
> - All of the code within this program was tested using Code Institute's PEP8.
> ![Tux, the Linux mascot](/readme.images/pep8.png)
> ![Tux, the Linux mascot](/readme.images/pep8.second.png)

> ## Bugs
 - **Resolved Bugs**
  - I missed capitalize (Style) in the print statement to color the header.It solved

     ![Tux, the Linux mascot](/readme.images/s.should.be.capital.png)
  - I found extra dot at the end of the input option. It solved.

      ![Tux, the Linux mascot](/readme.images/bug.extra.png)
- AttributeError: "str" object has no attribute "name".Then I ensure that the class is defined correctly and the name attribute is properly assigned in the __init__ method. it solved.

      ![Tux, the Linux mascot](/readme.images/bugs.python.png)
- Name: error "randint" is not defined, solved by typing correct name.  
      ![Tux, the Linux mascot](/readme.images/bug.randint.png)

- This error appear when I forgot to import the platform in the top of the file. It solved.
      ![Tux, the Linux mascot](/readme.images/platform.forgot.png)
- Indentation errors - Received indentation errors e.g "line code too long, over-indented and trailing whitespace" Fixed the indentation by ensuring all code lines in the functions were correctly aligned.
      ![Tux, the Linux mascot](/readme.images/indentation.png)   
- **Unsolved Bugs**
- Since the list has a greater height than the terminal window in Heroku, part of the list remains even after the window has been cleared. This behavior is not found when the application is run in, e.g., GitPod workspaces.

- ![Tux, the Linux mascot](/readme.images/twice.turn.png)


## Credits  
 - The main structure of this game coming from code institute. I used **Code Institute’s** code for my Battleships project to leverage their reliable solutions and best practices. This foundation provided proven techniques and efficient problem-solving. I then integrated my own code to customize and complete the project, ensuring it met specific requirements and aligned with Python programming goals. Here is the link to that page:".<https://learn.codeinstitute.net/courses/course-v1:CodeInstitute+PE_PAGPPF+2021_Q2/courseware/b3378fc1159e43e3b70916fdefdfae51/605f34e006594dc4ae19f5e60ec75e2e/>.
 - This video help me to understand basic of python, <https://www.youtube.com/watch?v=XKHEtdqhLK8>
 - Those two websites gave me ideas on how to Building the gameboard.
 - <https://teamtreehouse.com/community/dont-know-how-to-start-python-project-2-battleship>
 - <https://stackoverflow.com/questions/53446425/creating-a-row-of-numbers-letters-in-my-python-battleship-game>
 - For the functions, while loop, I have used stack overflow for idea.
 - Thanks to my friend, who can Python,(Talal Shemeri). Tt was great experience to discuss how functions and loops work in python.E-mail  **orange.2009@hotmail.com**

 

## **Acknowledgements**
 - I want to thank my mentor, **Luke Buchanan**, for his invaluable support and guidance during this project. His expertise was essential in overcoming challenges and improving the game.
 - Special thanks to my family for their support while I was deeply immersed in development. Their encouragement and belief in me have been a continual source of motivation."
 - I am deeply grateful for the wealth of resources and tutorials available online, which have been pivotal in acquiring the skills and knowledge necessary for this project. The open-source community and diverse educational platforms have played a crucial role in my development journey, providing invaluable support and inspiration.
 



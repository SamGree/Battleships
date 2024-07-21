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
    - You have to type - c -to continue then type player name to start the game, or - e - to exit.
  
## **Game Rules**
  - Board Size: The game is played on a 5x5 grid.
  - Ships: Each player has 5 ships.
  - Shots: Enter the row and column to make a shot (coordinates between 0 and 4).
  - Winning: Sink all the opponent's ships within 12 shots to win the game.
  - Type ( e ) to exit or ( c ) to start the game.
  > - ![Tux, the Linux mascot](/readme.images/run.program.png)

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
> - The user interface will be text-based, using print statements to display the game state and prompts for player input. The colorama library can be used to enhance the display with colors.
> - ![Tux, the Linux mascot](/readme.images/requirements.png)

## **Design**
#### **Flowchart**
- ![Tux, the Linux mascot](/readme.images/flowchart1.png)
## **import**
- os: used for adding a clear() function


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
> ![Tux, the Linux mascot](/readme.images/pep8.second.png)

> ## Bugs
 - Resolved Bugs
  - I missed i missed capitalize the first letter.It solved

     - ![Tux, the Linux mascot](/readme.images/s.should.be.capital.png)
  - I found extra dot at the end of input option. It solved.

     - ![Tux, the Linux mascot](/readme.images/bug.extra.png)
- AttributeError: "str" object has no attribute "name".Ensure 
  that the class is defined correctly and the name attribute is properly assigned in the __init__ method. it solved.

     - ![Tux, the Linux mascot](/readme.images/bugs.python.png)
- name: error "randint" is not defined, solved by typing correct name.  
     - ![Tux, the Linux mascot](/readme.images/bug.randint.png)

- This error appear when I forgot to import the platform statements in the top of the file. It solved.
     - ![Tux, the Linux mascot](/readme.images/platform.forgot.png)



## Credits
 - This video help me to understand basic of python <https://www.youtube.com/watch?v=XKHEtdqhLK8>
 - The main structure of this game coming from code institute including the codes but I have change or add some of the codes you will find comment next to the code.<https://learn.codeinstitute.net/courses/course-v1:CodeInstitute+PE_PAGPPF+2021_Q2/courseware/b3378fc1159e43e3b70916fdefdfae51/605f34e006594dc4ae19f5e60ec75e2e/>
 - Those two websites gave me ideas on how to create rows and columns.
 - <https://teamtreehouse.com/community/dont-know-how-to-start-python-project-2-battleship>
 - <https://stackoverflow.com/questions/53446425/creating-a-row-of-numbers-letters-in-my-python-battleship-game>

 

## **Acknowledgements**
 - Special thanks to my mentor **Luke Buchanan** for the feedback as always. 
 -  Thanks to **Tutor Assistance** for their constant support and guidance whenever I needed help.



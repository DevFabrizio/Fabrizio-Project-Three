# Fabrizio Milestone Project 3
#### [Link to Deployed Project]()
## Introduction
This the third project for the Code Institute Full Stack curriculum. Due to the fact that the only programming language used is Python, the project will mostly lack a modern user interface and will have little to no styling. These are the reasons why I have decided not to describe the project using the design principles used for all the previous websites I created. As a general overview this project is my first attempt at a terminal based game. I have decided to code a battleship game as suggested in the project ideas from Code Institute. This README file will contain description of the features and other details about my approach and specific content of the software.
## Project Goals
The main goals for this project is to create an entertaing game using the python programming language. Being this my first attempt at a project like this I have decided to implement simple features that would allow the user to experience a fluid gaming session. In addition to that the general aim was to provide game that would utilize user input to carry on the program until either the computer or the user reached a satisfactory condition (win or lose system).
### Target 
Given the almost legendary history of this game, the target audience is broadly represented by almost all ages. The game is relatively easily understood and the rules rarely create a barrier to the access of it. As a general rule of thumb I feel confident to say that this specific type of game can be played from anyone aged from 8 years old to 99+. For my version of the game the only impairment could be the language used.
## User Story
In order to better understand the flow of the game I will list the User Story as in the steps that the user will take to play the game.
As a User I want to:

* Read the instructions when the game starts 
* Input my battle name when presented with the user input on the terminal
* Allow the game to generate a grid for me and for the cpu
* Take mental note of the positions of my ships on the grid
* Input a number to target a specific row to hit
* Input a capital character to hit a specific column on the row I had previously chosen
* Evaluate if I hit or missed the enemy's ships
* Evaluate if the enemy hit or missed my ships
* Repeat the row and column selection until game completion

## Interactions and Features
Obviously the only interactions possible in a text based game that runs in a terminal are text input and some mouse clicking. When it comes to features though, I have decided to include some different solutions to make the game easy to understand for the user. Some of these features include validation of the user's input and a correct distribution of the text on the terminal.
### Features Used
### Future Features
The possible future features that could be implemented in the game are:
* The possibility to generate a custom sized grid through user input
* Creating a graphic interface in order to display the game on a UI instead that on the terminal
* Creating a function (or modifying an existing one) to limit the number of shots allowed
* Increasing the difficulty of the game by setting a time limit for every shot attempt
## Testing and Technologies
### Tech Used
The technologies and softwares used for this project are the following:
* CodeAnywhere as the IDE and code editor
* Heroku as the deployment platform
* Python Tutor as a tool to test partial code and review the flow of the program 
* GitHub as the repository holder
* [Tables Generator](https://tablesgenerator.com/) for the markdown table 
### Bugs
During the creation of this program I have encountered many bugs. I was able to fix them (some faster than others) with some Google searches or mainly just by going through the code. The majority of the bugs were caused by a mistake in indentation and targeting the wrong element. A valid "lesson learned" from this project is surely the fact that is important to go through your code line by line to make sure everything is working correctly.
### Validation
In order to validate the code a series of user input validation checks have been put into place to ensure a smooth run of the program.
The validatons are also necessary in order to allow the user to insert the correct data type or input. The following is a table with the validations applied:

| Validation         | Correct input            | Wrong input                                                                         | No input                          |   |
|--------------------|--------------------------|-------------------------------------------------------------------------------------|-----------------------------------|---|
| User battle name   | The game runs correctly  | The game gives suggestions on the correction to make.  Runs the input request again | The game waits for the user input |
| Row coordinates    | The game runs correctly  | The game alerts the user of the wrong input. Runs the input request again  | The game waits for the user input | 
| Column coordinates | The game runs correctly |  The game alerts the user of the wrong input. Runs the input request again  | The game waits for the user input | 
## Deployment and Updates
### Deployment Steps
## Development
### Software Maintenance and Updates
A correct indentation has been used in the code to allow future developers to maintain and update the code. In addition to that I have also used a series of functions to run specific parts of the game. These functions are then sequentially called in a general function that runs the main logic for the game. This structure makes it easier to modify the different functions to provide other functionality. It is also possible to modify the main logic of the game in the "run_game" function to twitch the flow of the game. 
## Credits
For this game I have used the following websites for development and testing:
* [Tables Generator](https://tablesgenerator.com/) for the markdown table.
* [Python Tutor](https://pythontutor.com/) for the debugging


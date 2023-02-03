# Egyptian Ratscrew Simulation Model
This repository contains a co-developed Agent Based model in Python that simulates games of Egyptian Ratscrew, a popular card game. The model is accompanied by an analysis class that provides insights into the win percentage of various strategies in the game.

## Getting Started
To run the simulation, download the model, analysis, and player files to your local machine. Then, run the model.py file to simulate games of Egyptian Ratscrew. To analyze the results of the simulations, run the analysis.py file. The PNG files in the analysis charts file provide further analysis of the game when certain variables are tested and compared.

## User Manual
###### Creating Players
To create a player, call the player function and pass in the following parameters: p.player(name, memorization skill, reaction skill, placing skill, miss slap skill). The skills should be rated on a scale from 1 to 10.

For example:
```python
playerOne = p.player("Player 1", 5,5,5,5)
playerTwo = p.player("Player 2", 5,5,5,5)
playerThree = p.player("Player 3", 5,5,5,5)
playerList = [playerOne,playerTwo,playerThree]
```

###### Simulating One Game
To simulate a single game and receive a play-by-play of every action, call the sim_one_game function and pass in a list of players. For example: sim_one_game(playerList, 1).

###### Simulating Multiple Games
To simulate a specified number of games, call the sim_x_games method and pass in the number of games you wish to simulate, as well as a list of players. For example: sim_x_games(100,playerList).


If you don't wish to manually create players, you can also call the dummy_player function in place of the playerList.

## Methodology
The ranges and values used to calculate the players' reaction, memorization, and placing skills were collected based on data gathered on card memorization amounts, placing times, and reaction times of the developers and other players. This includes chances to slap, misslap, and memorize cards.

## Contributors
This project was co-developed by Joshua Medvinsky and Daniel Penkov

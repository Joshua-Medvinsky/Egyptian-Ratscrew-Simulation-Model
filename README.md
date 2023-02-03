This project simulates games of Egyptian Ratscrew, a very common card game.

To run a simulation of an Egyptian Ratscrew run the model.py file.

For an analysis of the simulations run the analysis.py file.

The PNG's attached show analysis of when certain variables in the game are tested and compared.

User Manual:


When creating a player:
p.player(name, memorization skill, reaction skill, placing skill, miss slap skill)
(skills are from 1-10)
Creating players and playerList:
    playerOne = p.player("Player 1", 5,5,5,5)
    playerTwo = p.player("Player 2", 5,5,5,5)
    playerThree = p.player("Player 3", 5,5,5,5)
playerList = [playerOne,playerTwo,playerThree]

Utilizing sim_x_games function:
If the user wishes to simulate a certain number of games call the sim_x_games method and pass in the number of games you wish to simulate as well as a list of players you wish to call for this class
For example:
sim_x_games(100,playerList)

Utilizing sim_one_game function:
If a user wishes to simulate one game and receive a play by play for every action of the game the user can either call in sim_x_games and pass in 1 or directly call the sim_one_game	function as such:
sim_one_game(playerList, 1)

If a user doesn’t wish to manually create players they can also call and pass in the dummy_player() function in place of the playerList

All ranges and values used to calculate reaction, memorization, and placing performances were done in relation to data collected on card memorization amounts, placing times, and reaction times of us and other players. This includes chances to slap, misslap, and memorize cards.

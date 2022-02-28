# blitz-bot
This is the repository for the Discord bot, Blitz Bot. This was created using Python with the discord package. This repository is also hosted on Heroku for continuous deployment. 

Blitz Bot tracks the progress of users in a server in the games Wordle and Saltong. It also recognizes the most recent user who wasn't able to complete the game's puzzle and is thus called the "blitz".

## Commands
- !scores - Displays a leaderboard of users sorted by the highest scores
- !board - Displays a leaderboard of users sorted by the most "blitz" occurrences 
- !blitz - Displays the most recent "blitz" user

## How to use?
1. Clone repository to local machine
2. Type ```pip install discord``` on your command terminal
3. Type ```pip install dotenv``` on your command terminal
4. Create .env file at the root of the project
5. Create TOKEN variable inside .env file with the token of the Discord bot
6. Press run


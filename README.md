# ESP Game for Matching Images


## Problem 

Create an [ESP game](http://en.wikipedia.org/wiki/ESP_game) for Matching images. e.g. [Artigo](http://www.artigo.org/) is an esp game that is used for tagging.


## Problem Description/Rules

1. You need atleast two players paired to play this game at a time. 
2. Each player may not know whom they are paired with.
3. During the game play each paired player is shown the same question.
4. Each question would have a primary image and a set of secondary images to match to the primary image
5. Both paired players can move to the next question only when they choose the same set of secondary images


## TODO:

* [ ] Make user signup and login - *Not Required*
* [x] Create models for images (both primary and secondary)
* [x] Create basic routes and views
* [x] Create Express app
* [x] Implement sockets to make connection with client
* [x] Set up a DB for storing games and questions, maybe Mongo
* [x] Implement an Express routes to receive information from Django
* [x] Implement views for starting a new game 
* [ ] Delete game if any of the player disconnects
* [x] Wait for another player to join
* [x] Start game when two players are paired
* [x] Throw same question to paired players
* [ ] Let any player select an image and show message to second player
* [ ] Wait for responses, submit when both player choose the same image
* [ ] If both players select a different image, open the question for resubmission
* [ ] Move to next question on successful submit
* [ ] Update game table on game finish
* [ ] Self-pat
* [ ] Work on the UI
* [ ] Another self-pat

## Extending the Project:
* [ ] Make record getting more efficient (using order_by('?') atm)
* [ ] Handle client disconnect/ page refresh
* [ ] Use mongo/redis/postgres in place of sqlite

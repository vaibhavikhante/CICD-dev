
## Information

What do we expect?

 1. Actual working programs and containers
 1. Show us your best side

Stuck or need more information? Don't hesitate to contact us.

Once done, please notify us, so we can check out your work. We will get in touch with you as soon as possible.

## Part 1 - Python

We desperately need two Python servers that have nothing better to do than play number-guessing with each other. The first server serves as the "player" and the second as the "game master". Their common language is HTTP requests. We, as outsiders, can start a new round and watch how the two play with each other. The numbers are between 1 and 1000, but should be configurable.

Keep in mind, that these two servers are supposed to run in a Cloud-Environment.

### Player

The Player is a standalone python server that tries to find the number as fast as possible and plays with the Game Master without any interaction. We are just outsiders watching them play.

| Endpoint  | Response |
|---|---|
| /health | 200 - "healthy" |
| /hostname | 200 - \<server hostname\>  |
| /play | 200 - Result and history of the game |

If you need additional endpoints, feel free to implement them.

### Game Master

This is where you can get creative. We need a game master server, that is capable of playing multiple game sessions at once. The game master is picking a random number inside the range and answers with
- higher if the guessed number is too low
- lower if the guessed number is too high
- won if this is the number

## Part 2 - Docker
Dockerize your application and provide us with informations on how to build and run your docker images.
You can attach your documentation to this readme.

## Part 3 - Docker-Compose
Provide us with a docker-compose file for your game. It should contain healtchecks and configurations your game needs.
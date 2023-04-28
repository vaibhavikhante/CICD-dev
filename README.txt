number-guessing-game-two-player.py is create in python file
There are two player in this game Player one and Game Master. Playe rone will guess a number and then Game master has to guess same number range is between 1-1000.

Dockerfile will build the image which has the python file number-guessing-game-two-player.py

Docker-compose.yml will start container using this Docker file in location
'/usr/app/src/number-guessing-game-two-player.py'

#To build docker image we are using a python image from dockerhub so we will pull that image first
docker pull python:latest
docker image  build -t number-guess-game-two-player:11 .

#To start docker conatiner using teh image
docker container run -d -it number-guessing-game-two-player /bin/bash

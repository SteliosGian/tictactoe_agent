#!/bin/bash

EPS=0.1
ALPHA=0.5
DECAY=0.01
EPOCHS=10000

docker build -t tictactoe .

docker run -it tictactoe python3 play_game.py --eps ${EPS} --alpha ${ALPHA} --decay ${DECAY} --epochs ${EPOCHS}

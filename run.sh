#!/bin/bash

EPS=${1:-0.1}
ALPHA=${2:-0.5}
DECAY=${3:-0.01}
EPOCHS=${4:-10000}

docker build -t tictactoe .

echo "Epsilon value: ${EPS}"
echo "Alpha value: ${ALPHA}"
echo "Decay value: ${DECAY}"
echo "Epochs value: ${EPOCHS}"

docker run -it tictactoe python3 play_game.py --eps ${EPS} --alpha ${ALPHA} --decay ${DECAY} --epochs ${EPOCHS}

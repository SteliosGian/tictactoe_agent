# Tic Tac Toe Game

This repository trains an agent in the Tic Tac Toe game using Reinforcement Learning. <br>
<br>
The first step is to train the agent to learn to play the game. After the training, the human can play against the agent. <br>
<br>

To play the game, you need to have Docker installed.

<ul>
<li>Run the "run.sh" script</li>
<li>The board indices start from 0</li>
<li>The 1st square of the board is [0,0]</li>
</ul>

You can change the parameters of the agent by passing them as arguments to the script.
<br>
<br>
For example: "./run.sh 0.1, 0.5, 0.01, 10000"
<br>

#### Parameters
<ol>
<li>Epsilon: The epsilon value. How much will the agent select a random action. Default: 0.1. Range: 0-1</li>
<li>Alpha: The alpha value. The learning rate. Default: 0.5</li>
<li>Decay: The decay value. The value by which the epsilon will decrease at each iteration. Default: 0.01</li>
<li>Epochs: The number of iterations. Default: 10000</li>
</ol>

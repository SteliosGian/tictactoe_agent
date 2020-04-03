from __future__ import print_function
import numpy as np
import argparse
from agent import *
from env import *
from human import *

# recursive function that will return all
# possible states (as ints) and who the corresponding winner is for those states (if any)
# (i, j) refers to the next cell on the board to permute (we need to try -1, 0, 1)
# impossible games are ignored


def get_state_hash_and_winner(env, i=0, j=0):
    results = []

    for v in (0, env.x, env.o):
        env.board[i, j] = v  # if epty board it should already be 0
        if j == 2:
            # j goes back to 0, increase i, unless i = 2, then we are done
            if i == 2:
                # the board is full, collect results and return
                state = env.get_state()
                ended = env.game_over(force_recalculate=True)
                winner = env.winner
                results.append((state, winner, ended))
            else:
                results += get_state_hash_and_winner(env, i + 1, 0)
        else:
            # increment j, i stays the same
            results += get_state_hash_and_winner(env, i, j + 1)
    return results


def initialV_x(env, state_winner_triples):
    # initialize state values as follows
    # if x wins, V(s) = 1
    # if x loses or draw, V(s) = 0
    # otherwise, V(s) = 0.5
    V = np.zeros(env.num_states)
    for state, winner, ended in state_winner_triples:
        if ended:
            if winner == env.x:
                v = 1
            else:
                v = 0
        else:
            v = 0.5
        V[state] = v
    return V


def initialV_o(env, state_winner_triples):
    # this is (almost) the opposite of initial V for player x
    # since everywhere where x wins (1), o loses (0)
    # but a draw is still 0 for o
    V = np.zeros(env.num_states)
    for state, winner, ended in state_winner_triples:
        if ended:
            if winner == env.o:
                v = 1
            else:
                v = 0
        else:
            v = 0.5
        V[state] = v
    return V


def play_game(p1, p2, env, draw=False):
    # Loops until the game is over
    current_player = None
    while not env.game_over():
        # alternate between players
        # p1 always starts first
        if current_player == p1:
            current_player = p2
        else:
            current_player = p1

        # Draw the board before the user who wants to see it makes a move
        if draw:
            if draw == 1 and current_player == p1:
                env.draw_board()
            elif draw == 2 and current_player == p2:
                env.draw_board()

        # current player makes a move
        current_player.take_action(env)

        # Update state histories
        state = env.get_state()
        p1.update_state_history(state)
        p2.update_state_history(state)

    if draw:
        env.draw_board()

    # Do the value function update
    p1.update(env)
    p2.update(env)

def main(opts):
    # train the agent
    p1 = Agent(eps=opts.eps, alpha=opts.alpha, decay=opts.decay)
    p2 = Agent(eps=opts.eps, alpha=opts.alpha, decay=opts.decay)

    # set initial V for p1 and p2
    env = Environment()
    state_winner_triples = get_state_hash_and_winner(env)

    Vx = initialV_x(env, state_winner_triples)
    p1.setV(Vx)
    Vo = initialV_o(env, state_winner_triples)
    p2.setV(Vo)

    # give each player their symbol
    p1.set_symbol(env.x)
    p2.set_symbol(env.o)

    T = opts.epochs
    for t in range(T):
        if t % 200 == 0:
            print(t)
        play_game(p1, p2, Environment())

    # play human vs agent
    human = Human()
    human.set_symbol(env.o)
    while True:
        p1.set_verbose(True)
        play_game(p1, human, Environment(), draw=2)

        answer = input("Play again? [Y/n]: ")
        if answer and answer.lower()[0] == 'n':
            break


if __name__ == '__main__':
    """
    Parse cli arguments for converter
    """
    parser = argparse.ArgumentParser(description="Agent configuration")
    parser.add_argument("--eps", required=False, type=float, default=0.1, help="epsilon value")
    parser.add_argument("--alpha", required=False, type=float, default=0.5, help="alpha value")
    parser.add_argument("--decay", required=False, type=float, default=0.01, help="epsilon decay")
    parser.add_argument("--epochs", required=False, type=int, default=10000, help="number of iterations")
    args = parser.parse_args()
    main(args)





import numpy as np
import functools

ROLLS = np.array([3,4,5,6,7,8,9])
NEW_UNIVERSES = np.array([1,3,6,7,6,3,1])
WINNING_SCORE = 21
# ROLLS = np.array([3,4,5,6])
# NEW_UNIVERSES = np.array([1,3,3,1])

@functools.cache
def do_turn(score_p1, pos_p1, score_p2, pos_p2, player_turn):
    if player_turn == 1:
        score, pos, universes = perform_rolls(score_p1, pos_p1)
    else:
        score, pos, universes = perform_rolls(score_p2, pos_p2)

    wins = np.array([0,0])
    for i in range(len(score)):
        if score[i] >= WINNING_SCORE:
            wins[player_turn-1] += universes[i]
        else:
            if player_turn == 1:
                wins += universes[i] * do_turn(score[i], pos[i], score_p2, pos_p2, 2)
            else:
                wins += universes[i] * do_turn(score_p1, pos_p1, score[i], pos[i], 1)

    return wins

@functools.cache
def perform_rolls(score, pos):
    pos  = (pos + ROLLS - 1) % 10 + 1
    score += pos
    return score, pos, NEW_UNIVERSES
    
def main():
    score_p1 = 0
    score_p2 = 0
    pos_p1 = 2
    pos_p2 = 8

    wins = do_turn(score_p1, pos_p1, score_p2, pos_p2, 1)

    print(max(wins))

if __name__=="__main__":
    main()
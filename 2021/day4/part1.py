from itertools import islice
import numpy as np

def main():
    draws, boards, row_len = parse_input()

    winner = False
    points = 0
    for i in range(len(draws)):
        if not winner:
            for bd in boards:
                if not winner:
                    winner,points = check_winner([draws[x] for x in range(i+1)], bd, row_len)

    print(points)

def parse_input():
    with open('input.txt') as f:
        d = f.readlines()

    # first line is bingo draws
    draws = d[0].split(",")
    draws = [int(x) for x in draws]
    d.remove(d[0])
    # Clean up d
    d = [x for x in d if x != "\n"]

    # after are boards
    boards = [x.split() for x in d]
    row_len = len(boards[0])
    num_square_elems = row_len * row_len
    boards = [val for sublist in boards for val in sublist]
    boards = [int(x) for x in boards]
    iter_boards = iter(boards)
    boards = [list(islice(iter_boards,x)) for x in ([num_square_elems] * int(len(boards)/num_square_elems))]
    # boards = [np.array(x).reshape(row_len,row_len) for x in boards]

    return draws, boards, row_len

def check_winner(draws, board, row_len):
    winner = False
    points = -1

    board_match_index = [find_num_in_list(x, draws) for x in board]
    board_match_index_array = np.array(board_match_index).reshape(row_len,row_len)
    
    for i in range(row_len):
        if (sum(board_match_index_array[i]) == row_len) | (sum(board_match_index_array[:,i]) == row_len):
            winner = True
            points = sum([x*(1-y) for x,y in zip (board, board_match_index)]) * draws[-1]

    return winner, points

def find_num_in_list(num, list):
    if num in list:
        return 1
    else:
        return 0 

if __name__ == "__main__":
    main()

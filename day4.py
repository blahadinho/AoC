import pandas as pd
import numpy as np

def check_row(board):
    for row in board:
        if all(row):
            return True
    return False

def check_col(board):
    for col in range(len(board[0])):
        col_list = board[:, col]
        if all(col_list):
            return True
    return False

def check_boards(hit_boards):
    bingo = False
    winner = None
    for board_nbr, board in enumerate(hit_boards):
        row_bingo = check_row(board)
        col_bingo = check_col(board)
        if row_bingo | col_bingo:
            bingo = True
            winner = board_nbr
            return bingo, winner
    return bingo, winner

with open('input4.txt', 'r') as input3:
    lines = input3.read().split('\n')
lines.pop()

first = True
boards = []
i = -1
for line in lines:
    if first:
        row = [int(x) for x in line.split(',')]
        numbers = row
        first = False
        continue
    if line == '':
        boards.append([])
        i += 1
        continue
    else:
        row = [int(x) for x in line.split(' ') if x != '']
        boards[i].append(row)

nbr_boards = len(boards)
hit_boards = []
for i in range(nbr_boards):
    hit_boards.append(np.array(([False]*5, [False]*5, [False]*5, [False]*5, [False]*5)))


for number in numbers:
    for board_nbr, board in enumerate(boards):
        for row_nbr, row in enumerate(board):
            for col_nbr, element in enumerate(row):
                if element == number:
                    hit_boards[board_nbr][row_nbr][col_nbr] = True

    bingo, winner = check_boards(hit_boards)
    if bingo:
        winning_nbr = number
        print('BINGO! Winner is: ')
        print(winner)
        print('Winning number: ')
        print(winning_nbr)
        break

win_board = boards[winner]
win_hit_board = hit_boards[winner]

sum_unmark = 0
for row in range(5):
    for col in range(5):
        if not win_hit_board[row][col]:
            sum_unmark += win_board[row][col]

print(sum_unmark*winning_nbr)
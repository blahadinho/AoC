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

def check_boards(hit_board):
    bingo = False
    row_bingo = check_row(hit_board)
    col_bingo = check_col(hit_board)
    if row_bingo | col_bingo:
        bingo = True
    return bingo

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

nbr_boards = list(range(len(boards)))
hit_boards = []
for i in nbr_boards:
    hit_boards.append(np.array(([False]*5, [False]*5, [False]*5, [False]*5, [False]*5)))

won_boards = []
finish = False
for number in numbers:
    if finish:
        break
    for board_nbr, board in enumerate(boards):
        if board_nbr in won_boards:
            continue
        for row_nbr, row in enumerate(board):
            for col_nbr, element in enumerate(row):
                if element == number:
                    hit_boards[board_nbr][row_nbr][col_nbr] = True

        bingo = check_boards(hit_boards[board_nbr])
        if bingo:
            if len(nbr_boards) == 1:
                last_nbr = number
                last_board = board_nbr
                finish = True
                break
            nbr_boards.remove(board_nbr)
            won_boards.append(board_nbr)
            bingo = False

win_board = boards[last_board]
win_hit_board = hit_boards[last_board]

sum_unmark = 0
for row in range(5):
    for col in range(5):
        if not win_hit_board[row][col]:
            sum_unmark += win_board[row][col]

print(sum_unmark*last_nbr)
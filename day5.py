import numpy as np

with open('input5.txt', 'r') as input5:
    lines = input5.read().split('\n')
lines.pop()

pipes = []
for line in lines:
    pipe = line.split(' -> ')
    pipe_cord = [x.split(',') for x in pipe]
    pipe_start = [int(x) for x in pipe_cord[0]]
    pipe_end = [int(x) for x in pipe_cord[1]]
    pipes.append([pipe_start, pipe_end])

field = np.zeros([1000,1000])
for pipe in pipes:
    if pipe[0][0] == pipe[1][0]:
        row = pipe[0][0]
        col_start = min(pipe[0][1], pipe[1][1])
        col_stop = max(pipe[0][1], pipe[1][1])
        cols = list(range(col_start, col_stop+1))
        for col in cols:
            field[row][col] += 1
    elif pipe[0][1] == pipe[1][1]:
        col = pipe[0][1]
        row_start = min(pipe[0][0], pipe[1][0])
        row_stop = max(pipe[0][0], pipe[1][0])
        rows = list(range(row_start, row_stop+1))
        for row in rows:
            field[row][col] += 1
    else:
        row_start = pipe[0][0]
        row_stop = pipe[1][0]
        col_start = pipe[0][1]
        col_stop = pipe[1][1]
        row = row_start
        col = col_start
        while (row != row_stop) & (col != col_stop):
            field[row][col] += 1
            if row < row_stop:
                row += 1
            else:
                row -= 1
            if col < col_stop:
                col += 1
            else:
                col -= 1
        field[row][col] += 1
        

print(len(field[field>1]))
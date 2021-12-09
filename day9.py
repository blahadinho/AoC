import numpy as np

with open('input9.txt', 'r') as file:
    lines = file.read().split('\n')
lines.pop()

length = len(lines)
width = len(lines[0])

heightmap = np.zeros([length, width])
for i, line in enumerate(lines):
    heightmap[i] = [int(x) for x in line]

sum_lpoints = 0
for row in range(length):
    for col in range(width):
        if row == 0:
            if col == 0:
                if heightmap[row][col] < min([heightmap[row+1][col], heightmap[row][col+1]]):
                    sum_lpoints += heightmap[row][col]+1
            elif col == width-1:
                if heightmap[row][col] < min([heightmap[row+1][col], heightmap[row][col-1]]):
                    sum_lpoints += heightmap[row][col]+1
            else:
                if heightmap[row][col] < min([heightmap[row+1][col], heightmap[row][col+1], heightmap[row][col-1]]):
                    sum_lpoints += heightmap[row][col]+1
        elif row == length-1:
            if col == 0:
                if heightmap[row][col] < min([heightmap[row-1][col], heightmap[row][col+1]]):
                    sum_lpoints += heightmap[row][col]+1
            elif col == width-1:
                if heightmap[row][col] < min([heightmap[row-1][col], heightmap[row][col-1]]):
                    sum_lpoints += heightmap[row][col]+1
            else:
                if heightmap[row][col] < min([heightmap[row-1][col], heightmap[row][col+1], heightmap[row][col-1]]):
                    sum_lpoints += heightmap[row][col]+1
        else:
            if col == 0:
                if heightmap[row][col] < min([heightmap[row+1][col], heightmap[row-1][col], heightmap[row][col+1]]):
                    sum_lpoints += heightmap[row][col]+1
            elif col == width-1:
                if heightmap[row][col] < min([heightmap[row+1][col], heightmap[row-1][col], heightmap[row][col-1]]):
                    sum_lpoints += heightmap[row][col]+1
            else:
                if heightmap[row][col] < min([heightmap[row+1][col], heightmap[row-1][col], heightmap[row][col+1], heightmap[row][col-1]]):
                    sum_lpoints += heightmap[row][col]+1

print(sum_lpoints)

import numpy as np

def octoflash(octopuses, row, col, flashes, flashed_octos):
    flashes += 1
    flashed_octos[row][col] = True
    octopuses[flashed_octos] = 0
    octopuses[row][col] = 0
    for i in range(-1, 2):
        for j in range(-1, 2):
            octopuses[row+i][col+j] += 1
            if octopuses[row+i][col+j] >= 9:
                octopuses[flashed_octos] = 0
                octopuses[row][col] = 0
                octopuses, flashes = octoflash(octopuses, row+i, col+j, flashes, flashed_octos)
    return octopuses, flashes


with open('input11test2.txt', 'r') as file:
    lines = file.read().split('\n')

octopuses = np.zeros([len(lines), len(lines[0])])
for i, line in enumerate(lines):
    octopuses[i] = [int(x) for x in line]
length = len(octopuses)
width = len(octopuses[0])
octopuses = np.pad(octopuses, 1, constant_values=-float('inf'))
flashes_sum = 0
flashes = 0
for day in range(1,101):
    flashed_octos = np.zeros((length+2, width+2), dtype=bool)
    octopuses += 1
    while 9 <= np.max(octopuses):
        for row in range(1,length+1):
            for col in range(1,width+1):
                if octopuses[row][col] >= 9:
                    flashed_octos[row][col] = True
                    octopuses, flashes = octoflash(octopuses, row, col, flashes, flashed_octos)
                    flashes_sum += flashes
                    octopuses[flashed_octos] = 0

print(flashes_sum)
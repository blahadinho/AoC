import numpy as np
from queue import SimpleQueue

with open('input11.txt', 'r') as file:
    lines = file.read().split('\n')

octopuses = np.zeros([len(lines), len(lines[0])])
for i, line in enumerate(lines):
    octopuses[i] = [int(x) for x in line]
length = len(octopuses)
width = len(octopuses[0])
octopuses = np.pad(octopuses, 1, constant_values=-float('inf'))

queue = SimpleQueue()
flashes = 0
day = 0
not_sync = True
while not_sync:
    day += 1
    for row in range(1, length+1):
        for col in range(1, width+1):
            octopuses[row][col] += 1
            if octopuses[row][col] > 9:
                queue.put((row, col))
    
    while queue.qsize() > 0:
        (row, col) = queue.get()

        if octopuses[row][col] > 9:
            flashes += 1
            octopuses[row][col] = 0
            for i in range(-1, 2):
                for j in range(-1, 2):
                    if octopuses[row+i][col+j] != 0:
                        octopuses[row+i][col+j] += 1
                    if octopuses[row+i][col+j] > 9:
                        queue.put((row+i, col+j))

    if np.all((octopuses[1:length+1,1:width+1] == 0)):
        print(day)
        not_sync = False
        
print(flashes)
import numpy as np

def check_paths(caves, cur_cave, checked_caves, two_small):

    paths_ex = []
    if cur_cave.lower() == cur_cave:
        checked_caves.append(cur_cave)
    if cur_cave in caves:
        for next_cave in caves[cur_cave]:
            if next_cave in checked_caves:
                if (two_small) & (next_cave not in ['start', 'end']):
                    paths_ex.append(check_paths(caves, next_cave, checked_caves.copy(), False))
                else:
                    continue
            elif next_cave == 'end':
                paths_ex.append('end')
            else:
                paths_ex.append(check_paths(caves, next_cave, checked_caves.copy(), two_small))
    
    paths = []
    for line in paths_ex:
        if line == 'end':
            paths.append(cur_cave + '-' + line)
        elif line != []:
            for p in line:
                paths.append(cur_cave + '-' + p)
    return paths

with open('input12.txt', 'r') as file:
    lines = file.read().split('\n')
lines.pop()

caves = {}
for line in lines:
    cave = line.split('-')
    if cave[0] in caves:
        caves[cave[0]].append(cave[1])
    else:
        caves[cave[0]] = [cave[1]]
    if cave[1] in caves:
        caves[cave[1]].append(cave[0])
    else:
        caves[cave[1]] = [cave[0]]

checked_caves = ['start']
paths = []
for cur_cave in caves['start']:
    paths.append(check_paths(caves, cur_cave, checked_caves.copy(), True))

res = []
for line in paths:
    if line == 'end':
        res.append('start-' + line)
    elif line != []:
        for p in line:
            res.append('start-' + p)

    
print(len(res))
print(caves)
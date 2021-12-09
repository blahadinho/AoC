import numpy as np
import heapq

def check_basin(heightmap, point, width, length, checked_points):
    
    res = 0
    row = point[0]
    col = point[1]
    if (heightmap[row][col] == 9):
        return res
    else:
        checked_points.append((row,col))
        res += 1
    if (row+1,col) not in checked_points:
        res += check_basin(heightmap, (row+1, col), width, length, checked_points)
    if (row-1,col) not in checked_points:
        res += check_basin(heightmap, (row-1, col), width, length, checked_points)
    if (row,col+1) not in checked_points:
        res += check_basin(heightmap, (row, col+1), width, length, checked_points)
    if (row,col-1) not in checked_points:
        res += check_basin(heightmap, (row, col-1), width, length, checked_points)
    return res

with open('input9.txt', 'r') as file:
    lines = file.read().split('\n')
lines.pop()

length = len(lines)
width = len(lines[0])

heightmap = np.zeros([length, width])
for i, line in enumerate(lines):
    heightmap[i] = [int(x) for x in line]

heightmap = np.pad(heightmap, 1, constant_values=9,)

sum_lpoints = 0
low_point = []
for row in range(1,length+1):
    for col in range(1,width+1):

        if heightmap[row][col] < min([heightmap[row+1][col], heightmap[row-1][col], heightmap[row][col+1], heightmap[row][col-1]]):
            low_point.append((row, col))
            sum_lpoints += heightmap[row][col]+1

print(sum_lpoints)

basins = []
checked_points = []
for point in low_point:
    basins.append(check_basin(heightmap, point, width, length, checked_points))


print(heapq.nlargest(3, basins))
print(np.prod(heapq.nlargest(3, basins)))

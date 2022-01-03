import numpy as np
from queue import PriorityQueue

def get_neighbours(node):
    left = (node[0], node[1]-1)
    right = (node[0], node[1]+1)
    down = (node[0]+1, node[1])
    up = (node[0]-1, node[1])
    return [left, right, down, up]

with open('inputs/input15.txt', 'r') as file:
    lines = file.read().split('\n')
lines.pop()

grid = np.zeros([100, 100])
for row, line in enumerate(lines): grid[row] = [int(x) for x in line]
grid = np.pad(grid, 1, constant_values=float('inf'))

unvisited_nodes = []
for row in range(102):
    for col in range(102):
        unvisited_nodes.append((row, col))

dist_matrix = np.zeros([102, 102])
dist_matrix += float('inf')
dist_matrix[1][1] = 0

pq = PriorityQueue()
for node in unvisited_nodes:
    if node == (1, 1):
        pq.put((0, node))
    else:
        pq.put((float('inf'), node))


while not pq.empty():
    min_node = pq.get()
    node = min_node[1]
    if node == (100, 100):
        print(dist_matrix[node[0]][node[1]])
        break
    for next_node in get_neighbours(node):
        cur_dist = dist_matrix[node[0]][node[1]]
        next_dist = dist_matrix[next_node[0]][next_node[1]]
        if next_dist > cur_dist + grid[next_node[0]][next_node[1]]:
            dist_matrix[next_node[0]][next_node[1]] = cur_dist + grid[next_node[0]][next_node[1]]
            pq.put((dist_matrix[next_node[0]][next_node[1]], next_node))


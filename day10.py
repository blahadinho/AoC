import numpy as np
from collections import deque

with open('input10.txt', 'r') as file:
    lines_file = file.read().split('\n')
lines_file.pop()

lines = []
for line in lines_file:
    lines.append([x for x in line])

completion_score = []
mistakes_sum = 0
for line in lines:
    corrupt_line = False
    stack = deque()
    for char in line:
    
        if len(stack) == 0:
            stack.append(char)
        else:
            if char in [')', '}', ']', '>']:
                if stack[-1] == '(' and char == ')':
                    stack.pop()
                elif stack[-1] == '[' and char == ']':
                    stack.pop()
                elif stack[-1] == '{' and char == '}':
                    stack.pop()
                elif stack[-1] == '<' and char == '>':
                    stack.pop()
                else:
                    corrupt_line = True
                    if char == ')':
                        mistakes_sum += 3
                    elif char == ']':
                        mistakes_sum += 57
                    elif char == '}':
                        mistakes_sum += 1197
                    elif char == '>':
                        mistakes_sum += 25137
                    break
            else:
                stack.append(char)
    if not corrupt_line:
        score = 0
        while stack:
            missing = stack.pop()
            if missing == '(':
                score = score*5 + 1
            if missing == '[':
                score = score*5 + 2
            if missing == '{':
                score = score*5 + 3
            if missing == '<':
                score = score*5 + 4
        completion_score.append(score)

print(mistakes_sum)
print(np.median(completion_score))
print(np.sort(completion_score))
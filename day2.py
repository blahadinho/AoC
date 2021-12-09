with open('input2.txt', 'r') as input2:
    lines = input2.read().split('\n')

hori = 0
depth = 0
aim = 0
lines.pop()

for line in lines:
    command = line.split(' ')[0]
    value = int(line.split(' ')[1])
    if command == "forward":
        hori += value
        depth += aim * value
    elif command == 'down':
        aim += value
    elif command == 'up':
        aim -= value

print(hori)
print(depth)
print(hori*depth)
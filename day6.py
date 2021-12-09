with open('input6.txt', 'r') as input6:
    lines = input6.read().split('\n')
lines.pop()

fishes = [int(x) for x in lines[0].split(',')]
fish_dict = {0: 0, 1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0, 7: 0, 8: 0}

for fish in fishes:
    fish_dict[fish] += 1

for i in range(1,257):
    for i in range(9):
        if i == 0:
            temp = fish_dict[i]
        if i == 8:
            fish_dict[i] = temp
            fish_dict[6] += temp
        else:
            fish_dict[i] = fish_dict[i+1]
    
sum_fishes = 0
for i in range(9):
    sum_fishes += fish_dict[i]

print(sum_fishes)

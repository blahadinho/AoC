import matplotlib.pyplot as plt

with open('inputs/input13.txt', 'r') as file:
    lines = file.read().split('\n')
lines.pop()

dots = []
folds = []
time_for_folds = False
for line in lines:
    if line == '':
        time_for_folds = True
    else:
        if time_for_folds:
            if line.split('=')[0][-1] == 'x':
                folds.append((int(line.split('=')[-1]), 0))
            else:
                folds.append((int(line.split('=')[-1]), 1))    
        else:
            dot = [int(x) for x in line.split(',')]
            
            dots.append((dot[0], dot[1]))

dots_set = set(dots)
for fold in folds:
    fold_line = fold[0]
    x_or_y = fold[1]
    
    for nbr, dot in enumerate(dots):
        if dot[x_or_y] > fold_line:
            if x_or_y == 0:
                dots[nbr] = (fold_line-(dot[x_or_y]-fold_line), dot[1])
            else:
                dots[nbr] = (dot[0], fold_line-(dot[x_or_y]-fold_line))
    
    dots_set = set(dots)

x = []
y = []
for dot in dots_set:
    x.append(dot[0])
    y.append(-dot[1])
plt.scatter(x, y)
plt.show()


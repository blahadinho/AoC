def distance(crabs, target):
    eff_dist = 0
    for pos in crabs:
        dist = abs(pos-target)
        eff_dist += (dist**2 + dist)/2
    return eff_dist

with open('input7.txt', 'r') as input7:
    lines = input7.read().split('\n')
lines.pop()

crabs = [int(x) for x in lines[0].split(',')]

min_fuel = float('inf')
for target in range(min(crabs), max(crabs)+1):
    fuel = distance(crabs, target)
    if fuel < min_fuel:
        min_fuel = fuel

print(min_fuel)
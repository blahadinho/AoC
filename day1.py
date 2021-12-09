from numpy import loadtxt

data = loadtxt('input.txt')

prev_m = float('inf')
nbr_increases = 0
for m in data:
    if prev_m < m:
        nbr_increases += 1
    prev_m = m

print(len(data))
print(nbr_increases)


prev_wind = float('inf')
nbr_increased_wind = 0
for i in range(len(data)-2):
    wind = data[i] + data[i+1] + data[i+2]
    if prev_wind < wind:
        nbr_increased_wind += 1
    prev_wind = wind

print(nbr_increased_wind)
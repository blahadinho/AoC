
with open('input3.txt', 'r') as input3:
    lines = input3.read().split('\n')
lines.pop()

nbr_bits = len(lines[0])
nbr_lines = len(lines)
bits_count = [0]*nbr_bits

for line in lines:
    for i in range(nbr_bits):
        bits_count[i] += int(line[i])

for i, bit in enumerate(bits_count):
    if bit < nbr_lines/2:
        bits_count[i] = 0
    else:
        bits_count[i] = 1

print(bits_count)
gamma = sum(val*(2**idx) for idx, val in enumerate(reversed(bits_count)))
eps_bits_count = [abs(x-1) for x in bits_count]
eps = sum(val*(2**idx) for idx, val in enumerate(reversed(eps_bits_count)))

print(gamma*eps)


    
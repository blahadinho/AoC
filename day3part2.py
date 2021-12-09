with open('input3.txt', 'r') as input3:
    lines = input3.read().split('\n')
lines.pop()

nbr_bits = len(lines[0])
nbr_lines = len(lines)
bits_count = [0]*nbr_bits
j = 0

while nbr_lines != 1:

    bits_count = [0]*nbr_bits
    for line in lines:
        for i in range(nbr_bits):
            bits_count[i] += int(line[i])

    for i, bit in enumerate(bits_count):
        if bit == nbr_lines/2:
            bits_count[i] = 1
        elif bit < nbr_lines/2:
            bits_count[i] = 0
        else:
            bits_count[i] = 1
    
    new_lines = []
    for line in lines:
        if int(line[j]) == bits_count[j]:
            new_lines.append(line)
    
    lines = new_lines
    nbr_lines = len(lines)
    j += 1
oxygen = int(lines[0],2)
print(lines)


with open('input3.txt', 'r') as input3:
    lines = input3.read().split('\n')
lines.pop()

nbr_lines = len(lines)
bits_count = [0]*nbr_bits
j = 0

while nbr_lines != 1:

    bits_count = [0]*nbr_bits
    for line in lines:
        for i in range(nbr_bits):
            bits_count[i] += int(line[i])

    for i, bit in enumerate(bits_count):
        if bit == nbr_lines/2:
            bits_count[i] = 1
        elif bit < nbr_lines/2:
            bits_count[i] = 0
        else:
            bits_count[i] = 1
    
    new_lines = []
    for line in lines:
        if int(line[j]) != bits_count[j]:
            new_lines.append(line)
    
    lines = new_lines
    nbr_lines = len(lines)
    j += 1
co2 = int(lines[0],2)

print(lines)
print(oxygen)
print(co2)
print(oxygen*co2)
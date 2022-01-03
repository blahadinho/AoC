import numpy as np

def binaryToDecimal(binary):
     
    binary1 = binary
    decimal, i, n = 0, 0, 0
    while(binary != 0):
        dec = binary % 10
        decimal = decimal + dec * pow(2, i)
        binary = binary//10
        i += 1
    return decimal

with open('inputs/input16.txt', 'r') as file:
    lines = file.read().split('\n')
lines.pop()
hex_mes = lines[0]

bin_mes = ''

hex_to_bin = {'0': '0000', '1': '0001', '2': '0010', '3': '0011', '4': '0100', '5': '0101', '6': '0110', '7': '0111', '8': '1000', '9': '1001',
             'A': '1010', 'B': '1011', 'C': '1100', 'D': '1101', 'E': '1110', 'F': '1111'}
bin_to_hex = {}
for hex in hex_to_bin:
    bin_to_hex[hex_to_bin[hex]] = hex

for char in hex_mes:
    bin_mes = bin_mes + hex_to_bin[char]

version_sum = 0
version_nbr = bin_to_hex['0' + bin_mes[:3]]
version_sum += version_nbr
while False:
    version_nbr = bin_to_hex['0' + bin_mes[:3]]
    version_sum += version_nbr
    typeID = bin_to_hex['0' + bin_mes[3:6]]
    if typeID == '4':
        i = 0
        binary_value = ''
        while bin_mes[i*5+6] == '1':
            start = i*5+6
            binary_value = binary_value + bin_mes[start:start+4]
            i += 1
        start = i*5+6
        binary_value = binary_value + bin_mes[start:start+4]
        dicimal_value = binaryToDecimal(int(binary_value))
        end = start+5
        packet_len = np.ceil(end) * 4
        bin_mes = bin_mes[int(packet_len):]
    else:
        lenTypeID = bin_mes[6]

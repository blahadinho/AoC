def check_same(char, encoder):
    for x in set(char + encoder):
        if char.count(x) != encoder.count(x):
            return False
    return True

with open('input8.txt', 'r') as input8:
    lines = input8.read().split('\n')
lines.pop()

signals = []
outputs = []
for line in lines:

    signals.append(line.split(' | ')[0].split(' '))
    outputs.append(line.split(' | ')[1].split(' '))
print(len(outputs))


#for i in range(10): encode_digits[i] = None

sum_outputs = 0
for output, signal in zip(outputs, signals):
    
    encode_digits = {}
    for string in signal:
        if len(string) == 2:
            encode_digits[1] = [char for char in string]
        elif len(string) == 3:
            encode_digits[7] = [char for char in string]
        elif len(string) == 4:
            encode_digits[4] = [char for char in string]
        elif len(string) == 7:
            encode_digits[8] = [char for char in string]
    

    while len(encode_digits) != 10:
        for string in signal:
            char_list = [char for char in string]
            if len(char_list) == 5:
                if len([i for i in char_list if i in encode_digits[1]]) == 2:
                    encode_digits[3] = char_list
                if (len([i for i in char_list if i in encode_digits[4]]) == 3) & (len([i for i in char_list if i in encode_digits[1]]) == 1):
                    encode_digits[5] = char_list
                if len([i for i in char_list if i in encode_digits[4]]) == 2:
                    encode_digits[2] = char_list
            if len(char_list) == 6:
                if len([i for i in char_list if i in encode_digits[4]]) == 4:
                    encode_digits[9] = char_list
                if (len([i for i in char_list if i in encode_digits[1]]) == 2) & (len([i for i in char_list if i in encode_digits[4]]) == 3):
                    encode_digits[0] = char_list
                if len([i for i in char_list if i in encode_digits[1]]) == 1:
                    encode_digits[6] = char_list
    
    digits = []
    for string in output:
        char_list = [char for char in string]
        for j in range(10):
            if check_same(char_list, encode_digits[j]):
                digits.append(j)
    sum_outputs += 1000*digits[0]+100*digits[1]+10*digits[2]+digits[3]

print(sum_outputs)
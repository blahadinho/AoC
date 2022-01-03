from collections import defaultdict

with open('inputs/input14.txt', 'r') as file:
    lines = file.read().split('\n')
lines.pop()

first = True
rules = {}
pairs_count = defaultdict(int)
char_count = defaultdict(int)
for line in lines:
    if first:
        seq = [x for x in line]
        for i in range(len(seq)-1):
            pairs_count[seq[i] + seq[i+1]] += 1
            char_count[seq[i]] += 1
        char_count[seq[-1]] += 1
        first = False
    elif line != '':
        rule = line.split(' -> ')
        rules[rule[0]] = rule[1]


pairs = []
print(seq)
for step in range(40):

    
    for pair, count in pairs_count.copy().items():
        pairs_count[pair] -= count
        insert = rules[pair]
        pairs_count[insert + pair[1]] += count
        pairs_count[pair[0] + insert] += count
        char_count[insert] += count

print(max(char_count.values()) - min(char_count.values()))

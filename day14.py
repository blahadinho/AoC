with open('inputs/input14.txt', 'r') as file:
    lines = file.read().split('\n')
lines.pop()

first = True
rules = {}
for line in lines:
    if first:
        seq = [x for x in line]
        first = False
    elif line != '':
        rule = line.split(' -> ')
        rules[rule[0]] = rule[1]


pairs = []
print(seq)
for step in range(40):

    pairs = []
    for i in range(len(seq)-1):
        pairs.append(seq[i] + seq[i+1])
    
    for i in range(1, len(seq)):
        seq.insert(i*2-1, rules[pairs[i-1]])

    print('step: ' + str(step))
    print(len(seq))
    print(seq.count(max(set(seq), key=seq.count)))
    print(seq.count(min(set(seq), key=seq.count)))
    print(seq.count(max(set(seq), key=seq.count))-seq.count(min(set(seq), key=seq.count)))


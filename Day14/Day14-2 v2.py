with open('Day14 input.txt') as f:
    lines = f.readlines()


lines = [x.strip() for x in lines]
rules = dict()
for line in lines[lines.index('')+1:]:
    instructions = [x for x in line.split(' -> ')]
    rules[instructions[0]] = instructions[1]

start = lines[0]
counts = {k:0 for k in rules.keys()}
scores = {k:0 for k in set(rules.values())}

for i in range(len(start)-1):
    counts[start[i:i+2]] += 1
    scores[start[i]] += 1
scores[start[i+1]] += 1

for r in range(40):
    step = {k:0 for k in rules.keys()}
    for k,v in counts.items():
        step[k[0] + rules[k]] += v
        step[rules[k] + k[1]] += v
        scores[rules[k]] += v
    counts = step

order = [(k,v) for k,v in scores.items()]
order.sort(key=lambda x: x[1])
print(order[-1][1] - order[0][1])
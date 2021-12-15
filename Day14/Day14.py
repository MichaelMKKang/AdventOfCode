with open('Day14 input.txt') as f:
    lines = f.readlines()

lines = [x.strip() for x in lines]
rules = dict()
for line in lines[lines.index('')+1:]:
    instructions = [x for x in line.split(' -> ')]
    rules[instructions[0]] = instructions[1]

start = lines[0]

for i in range(10):
    step = ''
    for s in range(len(start)-1):
        try:
            step += start[s] + rules[start[s]+start[s+1]]
        except:
            step += start[s]
    step += start[s+1]
    start = step
    print(len(step))

from collections import Counter

counts = Counter(start)
most_to_least = [k for k,v in counts.most_common()]
print(counts[most_to_least[0]] - counts[most_to_least[-1]])
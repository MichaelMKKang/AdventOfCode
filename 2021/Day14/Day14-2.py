with open('Day14 input.txt') as f:
    lines = f.readlines()

def update_rules(chunk,rules):
    #if chunk in rules, return answer
    #if chunk not in rules, split chunk in two and do check again
    #   return the combined results
    #add the last char in chunk to end.
    try:
        return rules[chunk],rules
    except KeyError:
        try:
            mid = len(chunk)//2
            if len(chunk[:mid])==1:
                left = chunk[:mid]
            else:
                left,rules = update_rules(chunk[:mid],rules)
            right,rules = update_rules(chunk[mid:],rules)
            new = left + right
            #print(new,rules)
            new =  new + rules[chunk[-2:]]
            rules[chunk] = new
            print(chunk,new)
            return new,rules
        except:
            print('error')



lines = [x.strip() for x in lines]
rules = dict()
for line in lines[lines.index('')+1:]:
    instructions = [x for x in line.split(' -> ')]
    rules[instructions[0]] = instructions[0][0] + instructions[1]

start = lines[0]
for i in range(1,1+2):
    step = ''
    for s in range(0,len(start)-1,i):
        try:
            calc,rules = update_rules(start[s:s+i+1],rules)
            step += calc
            #print(start[s:s+i+1])
            #print(step)
        except:
            step += start[s]
    step += start[-1]
    start = step
    print(i,len(step))




from collections import Counter

counts = Counter(start)
most_to_least = [k for k,v in counts.most_common()]
print(counts[most_to_least[0]] - counts[most_to_least[-1]])

#every few steps, make a new dictionary of x sized string dict mappings, then iterate through respectively.

with open('Day7 input.txt') as f:
    lines = f.readlines()

crabs = [int(a) for a in lines[0].split(',')].copy()
crabs.sort()

dist_dict = {0:0}

for d in range(1,crabs[-1]+1):
    dist_dict[d] = dist_dict[d-1]+d


lowest_cost = float('inf')
best_loc = 0
for i in range(crabs[-1]):
    temp = sum([dist_dict[abs(c-i)] for c in crabs])
    if temp < lowest_cost:
        lowest_cost = temp
        best_loc = i

print(best_loc, lowest_cost)
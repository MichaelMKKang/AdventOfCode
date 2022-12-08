with open('Day7 input.txt') as f:
    lines = f.readlines()

crabs = [int(a) for a in lines[0].split(',')].copy()
crabs.sort()

lowest_cost = float('inf')
best_loc = 0
for i in range(crabs[-1]):
    temp = sum([abs(c-i) for c in crabs])
    if temp < lowest_cost:
        lowest_cost = temp
        best_loc = i

print(best_loc, lowest_cost)


def binary_search(crabs,crab_list):
    if len(crabs)==1:
        return crabs[0]
    left = crabs[:(len(crabs)//2)]
    right = crabs[(len(crabs)//2):]
    left_cost = sum([abs(c-(sum(left)/len(left))) for c in crab_list])
    right_cost = sum([abs(c-(sum(right)/len(right))) for c in crab_list])

    if left_cost == right_cost:
        return min(binary_search(left,crab_list), binary_search(right,crab_list))
    elif left_cost < right_cost:
        return binary_search(left,crab_list)
    else:
        return binary_search(right, crab_list)   

best_loc2 = binary_search(crabs,crabs)
lowest_cost2 = sum([abs(c-best_loc2) for c in crabs])

print(best_loc2, lowest_cost2)

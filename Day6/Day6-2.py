# NOTE: Need to have input have a newline character at the end
with open('Day6 input.txt') as f:
    lines = f.readlines()

population = [int(a) for a in lines[0].split(',')].copy()
print('Initial state: {}'.format(population))

frequencies = [0]*9
for p in population:
    frequencies[p] += 1

daycount = 0
for day in range(256):
    daycount += 1
    new_parents = frequencies.pop(0)
    frequencies[6] += new_parents
    frequencies.append(new_parents)
    print('After {} days: {} with {} new fish'.format(daycount,frequencies,new_parents))

print(sum(frequencies))

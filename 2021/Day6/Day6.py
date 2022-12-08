# NOTE: Need to have input have a newline character at the end
with open('Day6 input.txt') as f:
    lines = f.readlines()

population = [int(a) for a in lines[0].split(',')].copy()
print('Initial state: {}'.format(population))

daycount = 0
for day in range(80):
    next_gen = []
    new_fish = []
    for i in range(len(population)):
        population[i] -= 1
        if population[i] == 0:
            next_gen.append(population[i])
        elif population[i] < 0 :
            next_gen.append(6)
            new_fish.append(8)
        else:
            next_gen.append(population[i])
            
    next_gen += new_fish
    population = next_gen.copy()
    daycount += 1
    print('After {} days: {}'.format(daycount,population))
print(len(population))

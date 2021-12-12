import fuckit

with open('Day11 input.txt') as f:
    lines = f.readlines()

map = []
for line in lines:
    map.append([int(x) for x in list(line.strip())])

# return map with incremented energy
def increase_energy(map):
    return ([[x+1 for x in row] for row in map])

#return list of tuples of (row,col) format. to be used on what can't flash twice in one step
def find_flashes(map):
    flash_locs = []
    for r in range(len(map)):
        for c in range(len(map[r])):
            if map[r][c]>9:
                flash_locs.append((r,c))
    return flash_locs

#tries to increments everything around a coordinate by 1 and returns the updated map
#tried using fuckit library, but not sure why it wont return an object and dont want to find out now
def light_around(map,coord):
    try:
        if coord[0]-1 >= 0 and coord[1]-1 >= 0:
            map[coord[0]-1][coord[1]-1] += 1
    except:
        pass
    try:
        if coord[0]-1 >= 0:
            map[coord[0]-1][coord[1]] += 1
    except:
        pass
    try:
        if coord[0]-1 >= 0 and coord[1]+1 <= len(map[0]):
            map[coord[0]-1][coord[1]+1] += 1
    except:
        pass
    try:
        if coord[1]-1 >= 0:
            map[coord[0]][coord[1]-1] += 1
    except:
        pass
    try:
        if coord[1]+1 <= len(map[0]):
            map[coord[0]][coord[1]+1] += 1
    except:
        pass
    try:
        if coord[0]+1 <= len(map) and coord[1]-1 >= 0:
            map[coord[0]+1][coord[1]-1] += 1
    except:
        pass
    try:
        if coord[0]+1 <= len(map):
            map[coord[0]+1][coord[1]] += 1
    except:
        pass
    try:
        if coord[0]+1 <= len(map) and coord[1]+1 <= len(map[0]):
            map[coord[0]+1][coord[1]+1] += 1
    except:
        pass
    return map

#return map with any values > 9 set back to zero after flashing
def refractory(map):
    for r in range(len(map)):
        for c in range(len(map[r])):
            if map[r][c]>9:
                map[r][c] = 0
    return map

#True if fully synchronized
def check_syncro(map):
    for r in range(len(map)):
        for c in range(len(map[r])):
            if map[r][c]!=0:
                return False
    return True


#could do BFS or DFS, but dont want to implement. complexity doesn't get that much worse...
num_flashes = 0
for s in range(1,600+1):
    map = increase_energy(map)
    flashes = find_flashes(map)
    for f in flashes:
        map = light_around(map,f)
    prop_flashes = find_flashes(map)
    while len(prop_flashes) > len(flashes):
        new_flashes = [x for x in prop_flashes if x not in flashes]
        for f in new_flashes:
            map = light_around(map,f)
        flashes = prop_flashes
        prop_flashes = find_flashes(map)
    map = refractory(map)
    num_flashes += len(prop_flashes)
    if check_syncro(map):
        print('fully synchronized after step {}'.format(s))
        break

    #print('after step {}'.format(s))
    #for m in map:
    #    print(m)

print(num_flashes)

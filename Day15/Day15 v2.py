with open('Day15 input.txt') as f:
    lines = f.readlines()
lines = [x.strip() for x in lines]

#naive BFS search only keeping track of total risk
#but this can't go in a S-shape

#location being considered, the cost of moving there, and the path up to this point
active = [
    [(0,1),  int(lines[0][1]),  [(0,0)]],
    [(1,0),  int(lines[1][0]),  [(0,0)]],
]

completed_paths = []


#while there are still active items left (need to make sure to update min risk value after each completed one)
#while 1:
for i in range(3):
    possible_steps = []
    for a in active:
        coord = a[0]
        for r,c in [(0,1),(0,-1),(-1,0),(1,0)]:
            if (-1 < coord[0]+r < len(lines)) and (-1 < coord[1]+c < len(lines[0])) and ((coord[0]+r,coord[1]+c) not in a[2]):
                move = int(lines[coord[0]+r][coord[1]+c])
                possible_steps.append([ (coord[0]+r,coord[1]+c),  a[1] + move,  a[2] + [coord] ])

    min_heur = float('inf')
    mini = None
    for p in possible_steps:
        if (p[1]* ( (9-p[0][0])**2 + (9-p[0][1])**2)**0.5) < min_heur:
            min_heur = (p[1]* ( (9-p[0][0])**2 + (9-p[0][1])**2)**0.5)
            mini = p[1]
    #mini = min([x[1] for x in possible_steps])
    winners = []
    for p in possible_steps:
        if p[1] == mini:
            winners.append(p)
    #add round winners to active consideration list
    for w in winners:
        ind = None
        active.append(w)
        for a in range(len(active)):
            if (active[a][0] == w[2][-1]) and (active[a][2] == w[2][:-1]):
                ind = a
        #if ind is not None:
        #    _ = active.pop(ind)

    #remove any completed paths
    #NOTE: might need something if there are more than one path done at the same step
    done_inds = []
    for a in range(len(active)):
        if active[a][0] == (9,9):
            done_inds.append(a)
    if len(done_inds) != 0:
        for d in done_inds:
            completed_paths.append(active[d])
        active = [i for j, i in enumerate(active) if j not in done_inds]
    if len(active) == 0:
        break
    print(i)

for a in active:
    print(a)
print(' -- ')

for c in completed_paths:
    print(c)
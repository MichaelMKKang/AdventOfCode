class Cave:
    def __init__(self,name,size=1):
        self.name = name
        self.paths = []     #pointers to other cave objects
        self.size = size    #0 for small, 1 for large
        self.visited = 1    #not used for large caves

with open('Day12 input.txt') as f:
    lines = f.readlines()

lines = [x.strip() for x in lines]
segments = []
for line in lines:
    segments.append((line.split('-')[0],line.split('-')[1]))

cave_names = ['start']
start_cave = Cave('start',0)
start_cave.visited=1
caves = [start_cave]

for s in segments:
    for i in range(2):
        if s[i] not in cave_names:
            cave_names.append(s[i])
            caves.append(Cave(s[i],0 if s[i].islower() else 1))

for s in segments:
    cave0 = caves[cave_names.index(s[0])]
    cave1 = caves[cave_names.index(s[1])]
    if s[1] not in [x.name for x in cave0.paths]:
        cave0.paths.append(cave1)
    if s[0] not in [x.name for x in cave1.paths]:
        cave1.paths.append(cave0)


def dfs(cave,path,trips):
    if cave.size == 0:
        cave.visited -= 1
    if cave.name == 'end':
        trips.append(path+['end'])
        cave.visited += 1
        return trips
    for c in cave.paths:
        if c.visited > 0:
            trips = dfs(c, path+[cave.name],trips)
    cave.visited += 1
    return trips

path_list = []
#loop through and have one small cave at a time be visitable twice, then get rid of dupes
twice = [x.name for x in caves if x.name.islower() and x.name not in ['start','end']]
for t in twice:
    caves[cave_names.index(t)].visited += 1
    path_list = dfs(start_cave,[],path_list)
    caves[cave_names.index(t)].visited -= 1

import itertools
path_list.sort()
path_list = list(x for x,_ in itertools.groupby(path_list))

print(len(path_list))
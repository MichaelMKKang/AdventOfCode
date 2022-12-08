class Cave:
    def __init__(self,name,size=1):
        self.name = name
        self.paths = []     #pointers to other cave objects
        self.size = size    #0 for small, 1 for large
        self.visited = False

with open('Day12 input.txt') as f:
    lines = f.readlines()

lines = [x.strip() for x in lines]
segments = []
for line in lines:
    segments.append((line.split('-')[0],line.split('-')[1]))

cave_names = ['start']
start_cave = Cave('start',0)
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

#for c in caves:
#    print(c.name, ' : ', [x.name for x in c.paths])

def dfs(cave,path,trips):
    print('at cave',cave.name)
    if cave.size == 0:
        cave.visited = True
    if cave.name == 'end':
        trips.append(path+['end'])
        #print(trips)
        cave.visited = False
        return trips
    for c in cave.paths:
        if not c.visited:
            print('now visiting',c.name,' with a path of:',path+[cave.name])
            trips = dfs(c, path+[cave.name],trips)
    cave.visited = False
    return trips

path_list = dfs(start_cave,[],[])
print(len(path_list))
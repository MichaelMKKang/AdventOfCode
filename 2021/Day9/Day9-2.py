with open('Day9 input.txt') as f:
    lines = f.readlines()


map = []
for line in lines:
    map.append([int(x) for x in list(line.strip())])
lowest = []

#Trying to disprove that it is lowest. null hypothesis is that every point is lowest
for row in range(len(map)):
    for col in range(len(map[row])):
        islow = True
        #try left check
        try:
            if map[row][col] >= map[row][col-1] and col-1 >= 0:
                islow = False
        except:
            pass

        #try right check
        try:
            if map[row][col] >= map[row][col+1] and col+1 <= len(map[row]):
                islow=False
        except:
            pass
        
        #try top check
        try:
            if map[row][col] >= map[row-1][col] and row-1 >= 0:
                islow=False
        except:
            pass

        #try bot check
        try:
            if map[row][col] >= map[row+1][col] and row+1 <= len(map):
                islow=False
        except:
            pass

        if islow:
            lowest.append([row,col])

print(lowest)


from skimage.segmentation import flood

reduced_map = []
for m in map:
    reduced_map.append([x if x == 9 else 0 for x in m])

flood_sizes = []
for lows in lowest:
    flood_sizes.append(sum(sum(flood(reduced_map,tuple(lows), connectivity=1, tolerance=1))))


flood_sizes.sort()
print(flood_sizes)

print(flood_sizes[-1] * flood_sizes[-2] * flood_sizes[-3])
# NOTE: Need to have input have a newline character at the end
with open('Day5 input.txt') as f:
    lines = f.readlines()


#get largest x and largest y coordinates. then create map representation.
    #should have list of lists. list of rows (each element is a different row)
#iterate through lines and sum up the locations.

#get size2 list of tuples as a line, then list of lines
vents = []
max_rows = 0
max_cols = 0
for l in lines:
    segment = []
    coordinates = l.strip().split(' -> ')
    for c in coordinates:
        coords = c.split(', ')
        coords = coords[0].split(',')
        segment.append(coords)
        if int(coords[0]) > max_cols:
            max_cols = int(coords[0])
        if int(coords[1]) > max_rows:
            max_rows = int(coords[1])
    vents.append(segment)

#Make map. taking care not to create list with reference to the same value
map = [[0]*(max_cols+1) for _ in range(max_rows+1)]

#Only looking at vertical lines, then horizontal lines
for start,end in vents:
    if start[0]==end[0]:
        if int(start[1])>int(end[1]):
            start[1], end[1] = end[1], start[1]
        for i in range(int(start[1]),int(end[1])+1):
            map[i][int(start[0])] += 1
    if start[1]==end[1]:
        if int(start[0])>int(end[0]):
            start[0], end[0] = end[0], start[0]
        for j in range(int(start[0]), int(end[0])+1):
            map[int(start[1])][j] += 1

#Now check number of places where there is danger
count = 0 
for m in map:
    for n in m:
        if n > 1:
            count += 1
print(count)
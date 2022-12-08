with open('Day9 input.txt') as f:
    lines = f.readlines()


map = []
for line in lines:
    map.append([int(x) for x in list(line.strip())])

low_vals = []

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
            low_vals.append(int(map[row][col])+1)


print(low_vals)
print(sum(low_vals))
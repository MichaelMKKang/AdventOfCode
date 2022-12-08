with open('Day15 input.txt') as f:
    lines = f.readlines()
lines = [x.strip() for x in lines]

#only roughly remember dijkstra's algorithm and intentionally not looking it up again

# of coordinates:[total value risk if moved,and path so far]
#structure is...
# (consideration_coord_tuple):list(cum_risk_value,list(coord_path))
consider_dict = {(0,1):[int(lines[0][1]),[(0,0)]],(1,0):[int(lines[1][0]),[(0,0)]]}
visited_dict = {(0,0):True}
# for k in consider_dict:
#     visited_dict[k] = True

from copy import deepcopy

not_done = True
lowest_value = float('inf')
while not_done:
    new_dict = {}   #key is new_location, value is (summed risk, path). 
    for k in consider_dict:
        #print('looking out starting at',k[0],k[1])
        if k[0]+1 < len(lines) and (k[0]+1,k[1]) not in consider_dict[k][1]:
            down = int(lines[k[0]+1][k[1]])         #could make cleaner
            new_dict[(k[0]+1,k[1])] = deepcopy((consider_dict[k][0] + down,consider_dict[k][1]))   #c
            if new_dict[(k[0]+1,k[1])][1][-1] != k:
                new_dict[(k[0]+1,k[1])][1].append(k)
        if k[0]-1 > -1 and (k[0]-1,k[1]) not in consider_dict[k][1]:
            up = int(lines[k[0]-1][k[1]])
            new_dict[(k[0]-1,k[1])] = deepcopy((consider_dict[k][0] + up,consider_dict[k][1]))
            if new_dict[(k[0]-1,k[1])][1] != k:
                new_dict[(k[0]-1,k[1])][1].append(k)
        if k[1]+1 < len(lines[0]) and (k[0],k[1]+1) not in consider_dict[k][1]:
            right = int(lines[k[0]][k[1]+1])
            new_dict[(k[0],k[1]+1)] = deepcopy((consider_dict[k][0] + right,consider_dict[k][1]))
            if new_dict[(k[0],k[1]+1)][1] != k:
                new_dict[(k[0],k[1]+1)][1].append(k)
        if k[1]-1 > -1 and (k[0],k[1]-1) not in consider_dict[k][1]:
            left = int(lines[k[0]][k[1]-1])
            new_dict[(k[0],k[1]-1)] = deepcopy((consider_dict[k][0] + left,consider_dict[k][1]))
            if new_dict[(k[0],k[1]-1)][1] != k:
                new_dict[(k[0],k[1]-1)][1].append(k)
    #winner struct is...
    #list(tuple(new_dict_key,new_dict_value))
    winner = [(None,[float('inf'),[None]])]
    for k,v in new_dict.items():
        if v[0] <= winner[-1][1][0]:
            if winner[-1][1][1][0] is None:
                winner = [(k,v)]
            else:
                winner.append((k,v))
    for w in winner:
        if w[1][0]!= float('inf'):
            #print('winner',w)
            consider_dict[w[0]] = w[1]
            try:
                _ = consider_dict.pop(w[1][1][-1])
                #print('dict',consider_dict)
            except: pass
    lowest_value = min([val[0] if key==(9,9) else float('inf') for key,val in consider_dict.items()])
    if lowest_value < float('inf'):
        print(lowest_value)
    if (9,9) in consider_dict:
        _ = consider_dict.pop((9,9))
    if len(consider_dict.keys())==0:
        not_done = False
#concern about what happens if two paths hit the same point at the same time. old_loc gets overwritten
#a possible solution is to have the path as part of the key bundled as a tuple with the current loc

print(not_done)
import re
with open('Day17 input.txt') as f:
    lines = f.readlines()
lines = [x.strip() for x in lines]
line = lines[0][13:]
print(line)
x_range = re.search('(?<=x=).*(?=, )',line)[0]
x_range = [int(re.search('.*(?=\.\.)',x_range)[0]), int(re.search('(?<=\.\.).*',x_range)[0])]
print(x_range)
y_range = re.search('(?<=, y=).*',line)[0]
y_range = [int(re.search('.*(?=\.\.)',y_range)[0]), int(re.search('(?<=\.\.).*',y_range)[0])]
print(y_range)

#pos is (x,y), vel is (x_vel,y_vel)
# outputs new step,new vel
def step(x,y,x_vel,y_vel):
    new_x_pos = x + x_vel
    new_y_pos = y + y_vel
    y_vel -= 1
    if x_vel > 0:
        x_vel -= 1
    elif x_vel < 0:
        x_vel += 1
    else:
        pass
    return new_x_pos,new_y_pos,x_vel,y_vel

#returns 0 if winning shot, -1 if under, 1 if over, 2 if goes through
def try_shot(x,y,x_vel,y_vel):
    initial_y_vel = y_vel
    max_height = 0
    while x_vel != 0 or y >= y_range[0]:
        #step
        x,y,x_vel,y_vel = step(x,y,x_vel,y_vel)
        if y > max_height:
            max_height = y
        #print(x,y,x_vel,y_vel)
        #check for win
        if (x_range[0] <= x <= x_range[1]) and (y_range[0] <= y <= y_range[1]):
            print('y velocity ',initial_y_vel, ' has a max height of: ',max_height)
            return 0
        #every shot eventually gets to x_vel==0, but mercykill
        #if y_vel < 0 and y < y_range[0]:
        #    return -1
    #now x_vel == 0 and y_pos is under the box
    if x < x_range[0]:
        return -1
    elif x > x_range[1]:
        return 1
    else:
        return 2

direct_shot_counts = (x_range[1]-x_range[0]) * (y_range[1]-y_range[0])
print(direct_shot_counts)

max_height = 0
count = 0
winning_y_vels = []
x,y=0,0

for start_y_vel in range(-150,150):    #for each value of y_vel
    for start_x_vel in range(230):    #then just add by the # of direct shots
        x_vel,y_vel = start_x_vel,start_y_vel
        if try_shot(x,y,x_vel,y_vel) == 0:
            count += 1
    print('start y velocity: ',start_y_vel, 'with cumulative count ',count)


print(count)
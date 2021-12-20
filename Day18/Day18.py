import re
with open('Day18 input.txt') as f:
    lines = f.readlines()
given_lines = [x.strip() for x in lines]

#i is the index: the start of the first number once depth hit 5
def explode(snail,i):
    comma_index = i
    while snail[comma_index] != ',':
        comma_index += 1
        
    end_index = comma_index
    while snail[end_index] != ']':
        end_index += 1
    left_num = int(snail[i:comma_index])
    right_num = int(snail[comma_index+1:end_index])

    #first try exploding both ways, if error, then ...
    #try exploding left. if it doesn't work, then its gotta explode right
    try:
        left_index = i-1
        while snail[left_index] not in '0123456789':
            left_index -= 1
            if left_index < 0:
                raise Error
        left_left_index = left_index
        while snail[left_left_index] in '0123456789':
            left_left_index -= 1
        left_target = int(snail[left_left_index+1:left_index+1])
        right_index = end_index
        while snail[right_index] not in '0123456789':
            right_index += 1
            if right_index > len(snail):
                raise Error
        right_right_index = right_index
        while snail[right_right_index] in '0123456789':
            right_right_index += 1
        right_target = int(snail[right_index:right_right_index])
        #print('test',snail[left_index+1:i-1])
        new_snail = snail[:left_left_index+1] + str(left_num+left_target) + snail[left_index+1:i-1] + '0' + snail[end_index+1:right_index] + str(right_num+right_target) + snail[right_right_index:] 
            
    except:
        try:
            left_index = i-1
            while snail[left_index] not in '0123456789':
                left_index -= 1
                if left_index < 0:
                    raise Error
            left_left_index = left_index
            while snail[left_left_index] in '0123456789':
                left_left_index -= 1
            left_target = int(snail[left_left_index+1:left_index+1])
            new_snail = snail[:left_left_index+1] + str(left_num+left_target) + snail[left_index+1] + '0' + snail[end_index+1:]
            #print('only exploding left')
        except:
            try:
                right_index = end_index
                while snail[right_index] not in '0123456789':
                    right_index += 1
                    if right_index > len(snail):
                        raise Error
                right_right_index = right_index
                while snail[right_right_index] in '0123456789':
                    right_right_index += 1
                right_target = int(snail[right_index:right_right_index])
                new_snail = snail[:i-1] + '0' + snail[end_index+1:right_index] + str(right_num+right_target) + snail[right_right_index:]
                #print('only exploding right')
            except:
                print('bigger uhoh')
    snail = new_snail
    return snail

import math

#i is the index: the start of the first number where value > 9
def split(snail,i):
    num = int(snail[i:i+2])
    left = math.floor(num/2)
    right = math.ceil(num/2)
    return snail[:i] + '[' + str(left) + ',' + str(right) + ']' + snail[i+2:]

def step(line):
    depth = 0
    max_depth = 4
    max_depth_index = 0
    num = ''
    exploded = False
    for i in range(len(line)):
        if depth > max_depth:
            exploded = True
            max_depth = depth
            max_depth_index = i
        if line[i] == '[':
            depth += 1
        if line[i] == ']':
            depth -= 1
    if max_depth >= 5 and exploded:
        #print('max depth is',max_depth,'at index',max_depth_index)
        line = explode(line,max_depth_index)
        return line
    for i in range(len(line)):
        if line[i] in '0123456789':
            num += line[i]
            if int(num) > 9:
                #print(i)
                line = split(line,i-1)
                return line
        elif line[i] not in '0123456789' and num != '':
            num = ''
    return line


def snail_add(left,right):
    line = '[' + left + ',' + right + ']'
    #print(line)
    while 1:
        temp_line = step(line)
        if temp_line == line:
            break
        else:
            line = temp_line[:]
            #print(line)
    return line

def get_magnitude(line):
    depth = 0
    max_depth = 0
    max_depth_index = 0
    exploded = False
    for i in range(len(line)):
        if depth > max_depth:
            exploded = True
            max_depth = depth
            max_depth_index = i
        if line[i] == '[':
            depth += 1
        if line[i] == ']':
            depth -= 1
    #print(max_depth,max_depth_index)
    #print(line[max_depth])
    
    if max_depth == 0:
        return line
    
    comma_index = max_depth_index
    while line[comma_index] != ',':
        comma_index += 1
    #print(comma_index)
        
    end_index = comma_index
    while line[end_index] != ']':
        end_index += 1
    
    left_num = int(line[max_depth_index:comma_index])
    right_num = int(line[comma_index+1:end_index])
    
    #print(line[:max_depth_index-1])
    #print(left_num*3 + right_num*2)
    #print(line[end_index+1:])
    new_line = line[:max_depth_index-1] + str(left_num*3 + right_num*2) + line[end_index+1:]
    #print('new line:         ',new_line)
    return get_magnitude(new_line)

line = given_lines[0]
for l in given_lines[1:]:
    line = snail_add(line,l)
    #print(line)
print(get_magnitude(line))


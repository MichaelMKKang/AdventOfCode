with open('Day8 input.txt') as f:
    lines = f.readlines()

count = 0
for line in lines:
    output = line.split(' | ')[1].split(' ')
    for o in output:
        if len(o.strip()) in [2,4,3,7]:     #corresponding to 1,4,7,8 respectively
            print(o.strip())
            count += 1

print(count)

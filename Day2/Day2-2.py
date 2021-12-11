with open('Day2 input.txt') as f:
    lines = f.readlines()

dirs = [val.rstrip() for val in lines]

horz = 0
depth = 0
aim = 0

for d in dirs:
    a,b = d.split(' ')
    if a == 'forward':
        horz += int(b)
        depth += aim * int(b)
    elif a == 'down':
        aim += int(b)
    elif a == 'up':
        aim -= int(b)

    if aim<0:
        print('aim went negative')

print(horz)
print(depth)
with open('Day2 input.txt') as f:
    lines = f.readlines()

dirs = [val.rstrip() for val in lines]

horz = 0
depth = 0

for d in dirs:
    a,b = d.split(' ')
    if a == 'forward':
        horz += int(b)
    elif a == 'down':
        depth += int(b)
    elif a == 'up':
        depth -= int(b)

print(horz)
print(depth)
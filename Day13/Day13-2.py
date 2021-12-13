with open('Day13 input.txt') as f:
    lines = f.readlines()

lines = [x.strip() for x in lines]
dots = []
for line in lines[:lines.index('')]:
    dots.append(tuple([int(x) for x in line.split(',')]))

folds = []
for line in lines[lines.index('')+1:]:
    folds.append(tuple(line[11:].split('=')))

max_cols = max([x[0] for x in dots])+1
max_rows = max([x[1] for x in dots])+1

map = [[' ']*(max_cols) for _ in range(max_rows)]

for dot in dots:
    map[dot[1]][dot[0]] = '#'

# for m in map:
#     print(''.join(m))
# print('')

def fold_up(map,y):
    top = map[:y]
    bot = map[y+1:]
    bot.reverse()
    if len(top) > len(bot):
        diff = len(top) - len(bot)
        for d in range(diff):
            bot = ([' '] * len(bot)) + bot
    elif len(top) < len(bot):
        diff = len(bot) - len(top)
        for d in range(diff):
            top = ([' '] * len(top)) + top
    else:
        for i in range(len(top)):
            for j in range(len(top[0])):
                if len(bot) != len(top) or len(bot[i]) != len(top[i]):
                    print('error',len(map),len(bot),len(top),len(bot[i]),len(top[i]))
                if bot[i][j] == '#':
                    top[i][j] = '#'
    return top

def fold_left(map,x):
    new_left = []
    for row in range(len(map)):
        left = map[row][:x]
        right = map[row][x+1:]
        right.reverse()
        for r in range(len(left)):
            if right[r] == '#':
                left[r] = '#'
        new_left.append(left)
    return new_left

for f in folds:
    if f[0] == 'y':
        map = fold_up(map,int(f[1]))
    else:
        map = fold_left(map,int(f[1]))

for m in map:
     print(''.join(m))

count = 0
for i in map:
    for j in i:
        if j=='#':
            count += 1
print(count)
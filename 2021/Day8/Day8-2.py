with open('Day8 input.txt') as f:
    lines = f.readlines()

output_list = []

for line in lines: 
    digits = line.split(' | ')[0].split(' ')

    zerosixnine = []
    #Get BR and TR from one and two
    for d in digits:
        if len(d)==2:
            one = d
        if len(d)==3:
            seven = d
        if len(d)==4:
            four = d
        if len(d)==6:
            zerosixnine.append(d)

    for letter in ['a','b','c','d','e','f','g']:
        lettercount = 0
        for d in digits:
            if letter in d:
                lettercount += 1
        if lettercount == 9:
            BR = letter
    TR = one.replace(BR,'')  

    TOP = seven.replace(one[0],'').replace(one[1],'')

    #Using 0,6,9 vs the diff between 1 and 4 to find MID and TL
    tl_or_mid = four.replace(one[0],'').replace(one[1],'')
    for letter in tl_or_mid:
        lettercount = 0
        for d in zerosixnine:
            if letter in d:
                lettercount += 1
        if lettercount == 2:
            MID = letter
    TL = tl_or_mid.replace(MID,'')

    sixnine = [x for x in zerosixnine if MID in x]
    nine = [x for x in sixnine if TR in x]

    BL = [x for x in 'abcdefg' if x not in nine[0]][0]

    BOT = 'abcdefg'.replace(TOP,'').replace(MID,'').replace(TL,'').replace(BR,'').replace(TR,'').replace(BL,'')

    signal_dict = {
        ''.join(sorted(TOP+TL+TR+BL+BR+BOT))    :   0,
        ''.join(sorted(BR+TR))                  :   1,
        ''.join(sorted(TOP+TR+MID+BL+BOT))      :   2,
        ''.join(sorted(TOP+TR+MID+BR+BOT))      :   3,
        ''.join(sorted(TL+TR+MID+BR))           :   4,
        ''.join(sorted(TOP+TL+MID+BR+BOT))      :   5,
        ''.join(sorted(TOP+TL+MID+BR+BL+BOT))   :   6,
        ''.join(sorted(TOP+TR+BR))              :   7,
        ''.join(sorted('abcdefg'))              :   8,
        ''.join(sorted(TOP+TL+TR+MID+BR+BOT))   :   9
    }
        

    entry = ''
    output = line.split(' | ')[1].split(' ')
    for o in output:
        digit = ''.join(sorted(o.strip()))
        entry += str(signal_dict[digit])
    output_list.append(int(entry))

print(output_list)
print(sum(output_list))
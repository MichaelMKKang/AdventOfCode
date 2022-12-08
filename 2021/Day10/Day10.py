with open('Day10 input.txt') as f:
    lines = f.readlines()

line = '{([(<{}[<>[]}>{[]{[(<()>'   #corrupted
line = '<{([{{}}[<[[[<>{}]]]>[]]'     #incomplete

chunk_dict = {
    '(':')',
    '[':']',
    '{':'}',
    '<':'>'
}

score_dict = {
    ')':3,
    ']':57,
    '}':1197,
    '>':25137
}

score = 0
for line in lines:
    chunk = ''
    for l in line:
        if l in ['(','[','{','<']:
            chunk+=l
            print(chunk)
        if l in [')',']','}','>']:
            chunk, c = chunk[:-1], chunk[-1]
            if chunk_dict[c] != l:
                score += score_dict[l]
                print('Found an unexpected '+l)
                break
        
print(score)


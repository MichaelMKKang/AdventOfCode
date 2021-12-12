with open('Day10 input.txt') as f:
    lines = f.readlines()

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

corrupted = []

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
                corrupted.append(line)
                break
    
        
print(score)

incompletes = [x for x in lines if x not in corrupted]
inc_chunks = []

for inc in incompletes:
    chunk = ''
    for l in inc:
        if l in ['(','[','{','<']:
            chunk+=l
            print(chunk)
        if l in [')',']','}','>']:
            chunk = chunk[:-1]
    inc_chunks.append(chunk)

inc_score_dict = {
    '(':1,
    '[':2,
    '{':3,
    '<':4
}

inc_scores = []
for inc in inc_chunks:
    score = 0
    for i in inc[::-1]:
        score *= 5
        score += inc_score_dict[i]
    inc_scores.append(score)

inc_scores.sort()
print(inc_scores[(len(inc_scores)//2)])
import pandas as pd

with open('Day3 input.txt') as f:
    lines = f.readlines()

pos = [list(val.rstrip()) for val in lines]

df = pd.DataFrame(pos).astype(int)

gamma = ''
epsilon = ''

for c in df.columns:
    print(c, df[c].mode()[0])
    mode = df[c].mode()[0]
    gamma += str(mode)
    epsilon += '1' if mode==0 else '0'

print(gamma, epsilon)
print(int(gamma,2) * int(epsilon,2))
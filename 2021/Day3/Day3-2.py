import pandas as pd

with open('Day3 input.txt') as f:
    lines = f.readlines()

pos = [list(val.rstrip()) for val in lines]

oxygen = pd.DataFrame(pos).astype(int)
co2 = oxygen.copy(deep=True)

for o in oxygen.columns:
    if oxygen.shape[0]==1:
        break
    mode = oxygen[o].mode()
    if mode.shape[0]>1:
        oxygen = oxygen[oxygen[o]==1]
    else:
        oxygen = oxygen[oxygen[o]==mode[0]]
    print(oxygen)
    print('')


for c in co2.columns:
    if co2.shape[0]==1:
        break
    mode = co2[c].mode()
    if mode.shape[0]>1:
        co2 = co2[co2[c]==0]
    else:
        rev = 1 if mode[0]==0 else 0
        co2 = co2[co2[c]==rev]
    print(co2)
    print('')

oxygen_rating = int(''.join(str(x) for x in oxygen.values.tolist()[0]),2)
co2_rating = int(''.join(str(x) for x in co2.values.tolist()[0]),2)

print(oxygen_rating,co2_rating)
print(oxygen_rating * co2_rating)

'''
gamma = ''
epsilon = ''

for c in df.columns:
    print(c, df[c].mode()[0])
    mode = df[c].mode()[0]
    gamma += str(mode)
    epsilon += '1' if mode==0 else '0'

print(gamma, epsilon)
print(int(gamma,2) * int(epsilon,2))
'''
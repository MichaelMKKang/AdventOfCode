with open('Day1 input.txt') as f:
    lines = f.readlines()
nums = [int(val.rstrip()) for val in lines]

sums = []
for n in range(1,len(nums)-1):
    sums.append(nums[n-1]+nums[n]+nums[n+1])


inc = 0

for s in range(len(sums)-1):
    if sums[s]<sums[s+1]:
        inc+=1
print(inc)
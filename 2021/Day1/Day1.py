with open('Day1 input.txt') as f:
    lines = f.readlines()
nums = [int(val.rstrip()) for val in lines]

inc = 0

for n in range(len(nums)-1):
    if nums[n]<nums[n+1]:
        inc+=1
print(inc)
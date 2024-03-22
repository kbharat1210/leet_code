nums = [0,1,0,3,12]

i = len(nums)-1

while i >= 0:
    if nums[i] == 0:
        nums.append(nums.pop(i))
    i -= 1

print(nums)


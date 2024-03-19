nums = [3,1,2,10,1]

running_sum = []
sum = 0

for i in range(len(nums)):
    running_sum.append(nums[i]+sum)
    sum = nums[i] + sum
    i += 1
print(running_sum)
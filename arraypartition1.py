
nums = [6,2,6,5,1,2]
nums.sort()
nums.sort()

sublists = [nums[i:i + 2] for i in range(0, len(nums), 2)]
minimum_sum = sum(min(sublist) for sublist in sublists)

print(minimum_sum)







nums = [2,0,1,1,2]

for i in range(len(nums)):
    min_index =  i
    for j in range(i+1,len(nums)):
        if nums[j] < nums[min_index]:
            min_index = j

    nums[min_index], nums[i] = nums[i], nums[min_index]
print(nums)
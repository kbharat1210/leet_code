nums = [[2,8,7],[7,1,3],[1,9,5]]
s = 0
for num in nums:
     if s < sum(num):
        s = sum(num)
print(s)
def two_sum(numbers:list,target:int):

   for i in range(len(numbers)):
      for j in range(1,len(numbers)):
         if numbers[i] + numbers[j] == target:
            return [i+1,j+1]

s = two_sum([2,3,4],6)
print(s)










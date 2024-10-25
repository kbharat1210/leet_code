n = 10
count = 0



if n == 0 or n ==1:
    print(0)

for m in range(2,n):
    for i in range(2,int(m**0.5)+1):
        if m%i == 0:
            break
    else:
        count += 1
   
    
print(count)
        
            
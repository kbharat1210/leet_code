height = [1,1,4,2,1,3]
expected = sorted(height)

output = 0

for i in range(len(height)):
    if height[i] != expected[i]:
        output += 1
print(output)



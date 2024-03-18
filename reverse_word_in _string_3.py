s = "Let's take LeetCode contest"


substrings = s.split()


reverse_string =[]

for substring in substrings:
 reverse_string.append(''.join(reversed(substring)))

print(reverse_string)

out_string = ' '.join(reverse_string)
print(out_string)

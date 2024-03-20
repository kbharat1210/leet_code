n = 15
answer = []

for i in range(n):
    if (i + 1) % 3 == 0 and (i + 1) % 5 == 0:
        answer = answer + ["FizzBuzz"]
    elif (i + 1) % 3 == 0:
        answer = answer + ["Fizz"]
    elif (i + 1) % 5 == 0:
        answer = answer + ["Buzz"]
    else:
        answer = answer + [str(i+1)]

print(answer)
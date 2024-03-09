digits = [1,2,3]

digitsstr = ''.join(map(str,digits))

digitsint = int(digitsstr)
print(digitsint)

plusoneint= digitsint + 1
print(plusoneint)

plusonestr = str(plusoneint)
print(plusonestr)

plusonelist = list(plusonestr)
print(plusonelist)

plusone = list(map(int,plusonelist))
print(plusone)




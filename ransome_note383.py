ransome_note = "fihjjjjei"
magazine = "hjibagacbhadfaefdjaeaebgi"

d = dict()

for char in ransome_note:
    if char not in d:
        d[char] = 1
    else:
        d[char] = d[char] + 1
print(d)

d1 = {}
for char1 in magazine:
    if char1 not in d1:
        d1[char1] = 1
    else:
        d1[char1] = d1[char1] + 1
print(d1)

char_construct = True
for char, count in d.items():
    if char not in d1 or d1[char] < count:
        char_construct = False
        print(char_construct)
        break
if char_construct:
    print(char_construct)
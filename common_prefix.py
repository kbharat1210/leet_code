def common_prefix(strs):
    if not strs:
        return ""

    min_lenght = min(len(s) for s in strs)
    prefix = ""

    for i in range(min_lenght):
        char = strs[0][i]
        for j in range(1,len(strs)):
            if char != strs[j][i]:
                return prefix
        prefix += char

    return prefix

common = common_prefix(['flower','flow','flight'])
print(common)
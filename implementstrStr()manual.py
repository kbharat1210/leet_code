def implementstrStr(haystack:str,needle:str) -> int:
    for i in range(len(haystack)-len(needle)+1):
        if haystack[i:i+len(needle)] == needle:
            return i
    return -1

result = implementstrStr("programming is fun and challenging","fun")
print(result)






class Solution:
    def romanToInt(self, s: str) -> int:
        
        r2i = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        total = 0

        for i in range(len(s)):
            if i < len(s) - 1 and r2i[s[i]] < r2i[s[i + 1]]:
                total -= r2i[s[i]]
            else:
                total += r2i[s[i]]
        return total

class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        x = ''.join(char for char in s if char.isalnum())

        print(x)

        y = list(x)

        print(y)

        z = y[::-1]
        print(z)

        v = "".join(z)
        print(v)

        if x == v:
            return True

        else:
            return False

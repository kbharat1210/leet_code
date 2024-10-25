class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        if n<= 0:
            return False
        elif n == 1:
            return True

        for x in range(1,n):
            if 3**x == n:
                return True
            elif 3**x < n:
                pass
            elif 3**x > n:
                return False
                break



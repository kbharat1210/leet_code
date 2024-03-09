class Solution:
    def pivotIndex(self, nums: list[int]) -> int:
        s = sum(nums)
        leftsum = 0

        for i, x in enumerate(nums):
            if leftsum == (s - leftsum - x):
                return i
            else:
                leftsum += x
        return -1
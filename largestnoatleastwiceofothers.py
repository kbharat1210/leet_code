class Solution:
    def dominantIndex(self, nums: list[int]) -> int:
        maxvalue = max(nums)
        maxindex = nums.index(maxvalue)

        for i, num in enumerate(nums):
            if i != maxindex and maxvalue < 2 * num:
                return -1
        return maxindex

















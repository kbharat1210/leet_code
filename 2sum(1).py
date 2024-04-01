class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        matches = {}

        for i,number in enumerate(nums):
            match = target-number
            if match in matches:
                return[matches[match],i]
            else:
                matches[number] = i
        return []

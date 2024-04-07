def searchRange(nums, target):
    def findBound(nums, target, isFirst):
        left, right = 0, len(nums) - 1
        bound = -1

        while left <= right:
            mid = left + (right - left) // 2

            if target > nums[mid]:
                left = mid + 1
            elif target < nums[mid]:
                right = mid - 1
            else:
                bound = mid
                if isFirst:
                    right = mid - 1  # Search on the left side for the leftmost occurrence
                else:
                    left = mid + 1  # Search on the right side for the rightmost occurrence

        return bound

    left = findBound(nums, target, True)
    right = findBound(nums, target, False)

    return [left, right]
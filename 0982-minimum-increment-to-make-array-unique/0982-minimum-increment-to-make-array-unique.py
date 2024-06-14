class Solution(object):
    def minIncrementForUnique(self, nums):
        res = 0
        nums.sort()
        for i in range(1, len(nums)):
            if nums[i] - nums[i-1] < 1:
                to_inc = nums[i-1] + 1 - nums[i]
                nums[i] += to_inc
                res += to_inc
        return res

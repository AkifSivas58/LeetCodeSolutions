class Solution(object):
    def minDifference(self, nums):
        n = len(nums)
        if n <= 3:
            return 0
        
        nums.sort()
        
        # Calculate the four possible differences
        r1 = nums[n-1] - nums[3]
        r2 = nums[n-2] - nums[2]
        r3 = nums[n-3] - nums[1]
        r4 = nums[n-4] - nums[0]
        
        # Return the minimum difference
        return min(r1, r2, r3, r4)

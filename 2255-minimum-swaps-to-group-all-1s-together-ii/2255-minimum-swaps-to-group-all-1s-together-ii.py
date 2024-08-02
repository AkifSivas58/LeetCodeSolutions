class Solution(object):
    def minSwaps(self, nums):

        total = nums.count(1)

        nums.extend(nums)

        zeros = nums[:total].count(0)
        res = zeros

        for i in range(1, len(nums) - total + 1):
            if nums[i-1] == 0:
                zeros -= 1
            
            if nums[i + total -1] == 0:
                zeros += 1
        
            
            res = min(res, zeros)
        
        return res
        
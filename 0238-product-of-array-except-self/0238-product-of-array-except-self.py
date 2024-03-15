class Solution(object):
    def productExceptSelf(self, nums):
        res = []
        prefix = 1
        suffix = 1
        
        for i in range(len(nums)):
            res.append(prefix)
            prefix *= nums[i]
            
        for i in range(len(nums) - 1, -1, -1):
            res[i] *= suffix
            suffix *= nums[i]

        return res
            
            

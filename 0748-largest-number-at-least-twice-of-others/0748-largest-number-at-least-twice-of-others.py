class Solution(object):
    def dominantIndex(self, nums):
        maxInd = -1
        maxi = -1
        for i in range(len(nums)):
            if nums[i] > maxi:
                maxi = nums[i]
                maxInd = i
        
        for i in range(len(nums)):
            if i != maxInd and nums[i] * 2 > maxi:
                return -1
        
        return maxInd
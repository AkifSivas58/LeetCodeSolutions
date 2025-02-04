class Solution:
    def maxAscendingSum(self, nums: List[int]) -> int:
        curr = nums[0]
        maxi = curr
        for i in range(1, len(nums)):
            if nums[i] > nums[i-1]:
                curr += nums[i]
            else:
                curr = nums[i]
            
            maxi = max(maxi, curr)
        
        return maxi

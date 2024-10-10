class Solution:
    def maxWidthRamp(self, nums: List[int]) -> int:
        n = len(nums)
        rightMax = [None] * n
        rightMax[n-1] = nums[n-1]
        for i in range(n-2, -1, -1):
            rightMax[i] = max(rightMax[i+1], nums[i])
        
        maxi = 0
        l, r = 0, 0
        while r < n:
            if nums[l] > rightMax[r]:
                l += 1
                continue
            
            maxi = max(maxi, r-l)
            r += 1
        
        return maxi

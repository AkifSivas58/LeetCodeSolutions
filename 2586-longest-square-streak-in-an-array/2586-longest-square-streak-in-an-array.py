class Solution:
    def longestSquareStreak(self, nums: List[int]) -> int:
        n = len(nums)
        nums.sort()
        sett = set(nums)
        
        res = 1
        for i in range(n):
            lenn = 1
            x = nums[i]
            while x ** 2 in sett:
                lenn += 1
                x = x ** 2
            
            res = max(res, lenn)
        
        return res if res > 1 else -1
        

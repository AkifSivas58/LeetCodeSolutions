class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        maxi = max(nums)
        length = 0
        res = 0
        for i in range(len(nums)):
            if nums[i] == maxi:
                length += 1
            else:
                length = 0
            
            res = max(res, length)
        return res
class Solution:
    def minSubarray(self, nums: List[int], p: int) -> int:
        target = sum(nums) % p
        pref = 0
        pref_mod = {0 : -1}
        res = len(nums)
        
        if target == 0:
            return 0
            
        for i in range(len(nums)):
            pref = (pref + nums[i]) % p
            needed = (pref - target) % p
            if needed in pref_mod:
                res = min(res, i - pref_mod[needed])
            
            pref_mod[pref] = i
        
        if res < len(nums):
            return res
        else:
            return -1
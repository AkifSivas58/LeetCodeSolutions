class Solution:
    def findPrefixScore(self, nums: List[int]) -> List[int]:
        n = len(nums)

        maxi = 0
        conver = [0] * n
        for i in range(n):
            maxi = max(maxi, nums[i])
            conver[i] = nums[i] + maxi
        
        pref = [0] * n
        pref[0] = conver[0]
        for i in range(1, n):
            pref[i] = pref[i-1] + conver[i]
        
        return pref

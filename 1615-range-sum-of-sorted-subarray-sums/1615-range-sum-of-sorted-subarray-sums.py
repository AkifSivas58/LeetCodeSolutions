class Solution(object):
    def rangeSum(self, nums, n, left, right):
        mod = 10**9 + 7
        pref = [0] * (n+1)
        for i in range(1, n+1):
            pref[i] = pref[i-1] + nums[i-1]
        
        for i in range(1, n+1):
            for j in range(i+1, n+1):
                pref.append(pref[j] - pref[i])
        
        pref.sort()

        res = sum(pref[left:right+1])
        return res % mod
class Solution(object):
    def distinctDifferenceArray(self, nums):
    
        res = []
        for i in range(len(nums)):
            prefix = set()
            sufix = set()
            prefix.add(nums[i])
            for pref in nums[:i]:
                prefix.add(pref)

            for suff in nums[i+1:]:
                sufix.add(suff)

            res.append(len(prefix) - len(sufix))

        return res
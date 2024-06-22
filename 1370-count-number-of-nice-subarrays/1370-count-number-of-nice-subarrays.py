class Solution(object):
    def numberOfSubarrays(self, nums, k):
        res = 0
        odds = 0
        prefs = {0 : 1}
        for num in nums:
            if num % 2 == 1:
                odds += 1

            if odds - k in prefs:
                res += prefs[odds-k]

            if odds in prefs:
                prefs[odds] += 1
            else:
                prefs[odds] = 1

        return res
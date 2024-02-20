class Solution(object):
    def missingNumber(self, nums):
        if 0 not in nums:
            return 0
        n = max(nums)
        expected_sum = (n*(n+1)) / 2
        got_sum = 0
        for i in nums:
            got_sum += i
        sol = expected_sum - got_sum

        if sol == 0:
            return n+1
        else:
            return sol
        
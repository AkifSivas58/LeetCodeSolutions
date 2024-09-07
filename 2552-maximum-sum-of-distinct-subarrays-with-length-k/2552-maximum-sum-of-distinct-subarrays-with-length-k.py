from collections import Counter
class Solution(object):
    def maximumSubarraySum(self, nums, k):
        res = 0
        curr = 0
        count = Counter()

        for i in range(k):
            count[nums[i]] += 1
            curr += nums[i]

        if len(count) == k:
            res = curr

        for i in range(k, len(nums)):
            count[nums[i]] += 1
            curr += nums[i]

            count[nums[i - k]] -= 1
            if count[nums[i - k]] == 0:
                del count[nums[i - k]]
            curr -= nums[i-k]
            if len(count) == k:
                res = max(res, curr)
        
        return res
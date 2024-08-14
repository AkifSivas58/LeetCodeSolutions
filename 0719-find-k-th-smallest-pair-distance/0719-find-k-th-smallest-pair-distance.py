class Solution(object):
    def smallestDistancePair(self, nums, k):
        nums.sort()
        l = 0
        r = nums[-1] - nums[0]
        
        while l < r:
            m = (l+r) // 2

            count = 0
            j = 0
            for i in range(len(nums)):
                while j < len(nums) and nums[j]-nums[i] <= m:
                    j += 1
                count += j - i - 1


            if count >= k:
                r = m
            else:
                l = m + 1
        
        return l
        
        
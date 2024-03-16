class Solution(object):
    def findMaxLength(self, nums):
        counts = {0 : -1}
        res = 0
        sums = 0
        for i in range(len(nums)):
            if nums[i] == 0:
                sums -= 1
            else:
                sums += 1
            
            if sums in counts:
                res = max(res, i - counts[sums])
            else:
                counts[sums] = i

        return res

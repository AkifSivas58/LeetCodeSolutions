from collections import defaultdict
class Solution(object):
    def sortColors(self, nums):
        counts = defaultdict(int)
        for num in nums:
            counts[num] += 1
        
        nums[:] = []
        nums.extend([0] * counts[0])
        nums.extend([1] * counts[1])
        nums.extend([2] * counts[2])
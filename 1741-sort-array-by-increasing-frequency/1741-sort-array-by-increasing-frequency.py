from collections import Counter
class Solution(object):
    def frequencySort(self, nums):
        counts = Counter(nums)
        
        nums.sort(key=lambda x: (counts[x], -x))

        return nums
import heapq
class Solution(object):
    def sortArray(self, nums):
        heapq.heapify(nums)
        res = []
        while nums:
            num = heapq.heappop(nums)
            res.append(num)
        
        return res
        
import heapq
import math
class Solution:
    def maxKelements(self, nums: List[int], k: int) -> int:
        pq = []
        heapq.heapify(pq)
        for num in nums:
            heapq.heappush(pq, -num)
        score = 0
        for _ in range(k):
            val = -heapq.heappop(pq)
            score += val
            val /= 3
            val = math.ceil(val)
            heapq.heappush(pq, -val)
        
        return score

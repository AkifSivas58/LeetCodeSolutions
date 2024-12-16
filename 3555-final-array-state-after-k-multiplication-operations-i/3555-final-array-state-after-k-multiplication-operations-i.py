import heapq
class Solution:
    def getFinalState(self, nums: List[int], k: int, multiplier: int) -> List[int]:
        pq = []

        for i in range(len(nums)):
            heapq.heappush(pq, (nums[i], i))
        
        print(pq)
        for _ in range(k):
            num, i = heapq.heappop(pq)
            new_num = num * multiplier
            nums[i] = new_num
            heapq.heappush(pq, (nums[i], i))
        
        return nums
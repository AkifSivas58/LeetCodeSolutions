import heapq
class Solution:
    def smallestRange(self, nums: List[List[int]]) -> List[int]:
        pq = []
        heapq.heapify(pq)
        cur_max = float('-inf')
        start, end = float('-inf'), float('inf')
        k = len(nums)
        for i in range(k):
            heapq.heappush(pq, (nums[i][0], i, 0))
            cur_max = max(cur_max, nums[i][0])


        while len(pq) == k:
            cur_min, list_ind, ind = heapq.heappop(pq)
            if cur_max - cur_min < end - start:
                start = cur_min
                end = cur_max
            
            if len(nums[list_ind]) > ind + 1:
                heapq.heappush(pq, (nums[list_ind][ind+1], list_ind, ind+1))
                cur_max = max(cur_max, nums[list_ind][ind+1])
            
        return [start, end]
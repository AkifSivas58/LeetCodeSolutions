import heapq
class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        res = ""
        pq = [(-a, "a"), (-b, "b"), (-c, "c")]
        pq = [(count, ch) for count, ch in pq if count != 0]
        heapq.heapify(pq)
        while pq:
            count, ch = heapq.heappop(pq)
            count *= -1
            if len(res) >= 2 and res[-1] == res[-2] == ch:
                if not pq:
                    break

                other_count, other_ch = heapq.heappop(pq)
                other_count *= -1 
                
                res = res + other_ch
                other_count -= 1
                
                if other_count > 0:
                    heapq.heappush(pq, (-other_count, other_ch))
                heapq.heappush(pq, (-count, ch))
            else:
                res = res + ch
                count -= 1
                if count > 0:
                    heapq.heappush(pq, (-count, ch))
        
        return res
            


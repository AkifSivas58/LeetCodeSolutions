import heapq
class Solution:
    def repeatLimitedString(self, s: str, repeatLimit: int) -> str:
        freq = dict()
        for c in s:
            if c not in freq:
                freq[c] = 1
            else:
                freq[c] += 1

        pq = [(-ord(c), c, count) for c, count in freq.items()]
        heapq.heapify(pq)

        res = []
        while pq:
            val, char, count = heapq.heappop(pq)

            max_add = min(count, repeatLimit)
            res.extend([char] * max_add)

            if count > max_add:
                if not pq:
                    break
                
                next_val, next_char, next_count = heapq.heappop(pq)
                res.append(next_char)
                heapq.heappush(pq, (val, char, count - max_add))

                if next_count > 1:
                    heapq.heappush(pq, (next_val, next_char, next_count - 1))
        
        return "".join(res)

        
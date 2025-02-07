from collections import defaultdict
class Solution:
    def queryResults(self, limit: int, queries: List[List[int]]) -> List[int]:
        res = []
        colors = defaultdict(int)
        balls = defaultdict(int)
        curr = 0
        for x, y in queries:
            
            if colors[x] != 0:
                balls[colors[x]] -= 1
                if balls[colors[x]] == 0:
                    curr -= 1

            if balls[y] == 0:
                curr += 1

            balls[y] += 1
            colors[x] = y
            res.append(curr)

        return res
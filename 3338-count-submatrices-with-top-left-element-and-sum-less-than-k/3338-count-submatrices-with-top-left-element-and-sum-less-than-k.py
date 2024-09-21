class Solution:
    def countSubmatrices(self, grid: List[List[int]], k: int) -> int:
        m = len(grid)
        n = len(grid[0])
        pref = [[0] * n for _ in range(m)]
        pref[0][0] = grid[0][0]
        for i in range(1, m):
            pref[i][0] = pref[i-1][0] + grid[i][0]
        
        for j in range(1, n):
            pref[0][j] = pref[0][j-1] + grid[0][j]
        
        for i in range(1, m):
            for j in range(1, n):
                pref[i][j] = pref[i-1][j] + pref[i][j-1] - pref[i-1][j-1] + grid[i][j]
        
        res = 0
        for i in range(m):
            for j in range(n):
                if pref[i][j] <= k:
                    res += 1
        
        return res
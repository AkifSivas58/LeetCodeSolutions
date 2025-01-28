from typing import List

class Solution:
    def findMaxFish(self, grid: List[List[int]]) -> int:
        def dfs(x, y, visited):
            if (
                x < 0 or x >= len(grid) or 
                y < 0 or y >= len(grid[0]) or 
                (x, y) in visited or 
                grid[x][y] == 0
            ):
                return 0

            visited.add((x, y))
            total_fish = grid[x][y]

            total_fish += dfs(x, y + 1, visited)
            total_fish += dfs(x, y - 1, visited)
            total_fish += dfs(x + 1, y, visited)
            total_fish += dfs(x - 1, y, visited)

            return total_fish
        
        max_fish = 0

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] != 0: 
                    max_fish = max(max_fish, dfs(i, j, set()))

        return max_fish

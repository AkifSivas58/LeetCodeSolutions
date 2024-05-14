class Solution(object):
    def matrixScore(self, grid):
        for i in range(len(grid)):
            if grid[i][0] == 0:
                for j in range(len(grid[0])):
                    if grid[i][j] == 0:
                        grid[i][j] = 1
                    else:
                        grid[i][j] = 0
            
        for j in range(len(grid[0])):
            zeros = 0
            ones = 0
            for i in range(len(grid)):
                if grid[i][j] == 1:
                    ones += 1
                else:
                    zeros += 1
            
            if ones < zeros:
                for i in range(len(grid)):
                    if grid[i][j] == 1:
                        grid[i][j] = 0
                    else:
                        grid[i][j] = 1

        result = 0
        for row in grid:
            for j in range(len(row)):
                if row[j] == 1:
                    result += 2 ** (len(row) - 1 -j)
        return result
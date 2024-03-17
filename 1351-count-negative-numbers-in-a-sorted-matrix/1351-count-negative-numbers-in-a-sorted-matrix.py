class Solution(object):
    def countNegatives(self, grid):
        count = 0
        for row in grid:
            for col in row:
                if col < 0:
                    count += 1

        return count
        
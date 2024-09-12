from typing import List

class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        matrix = [[0] * n for _ in range(n)]

        up = 0
        down = n - 1
        left = 0
        right = n - 1
        
        i, j = 0, 0
        di, dj = 0, 1
        curr = 1

        while curr <= n ** 2:
            matrix[i][j] = curr
            curr += 1
            
            ni, nj = i + di, j + dj
            
            if nj > right: 
                di, dj = 1, 0
                up += 1
            elif ni > down:
                di, dj = 0, -1
                right -= 1
            elif nj < left:
                di, dj = -1, 0
                down -= 1
            elif ni < up:
                di, dj = 0, 1
                left += 1
            else:
                i, j = ni, nj
                continue

            i += di
            j += dj
        
        return matrix

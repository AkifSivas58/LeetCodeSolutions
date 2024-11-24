class Solution:
    def maxMatrixSum(self, matrix: List[List[int]]) -> int:
        n = len(matrix)
        nega_count = 0
        absolute = float('inf')
        summ = 0

        for i in range(n):
            for j in range(n):
                summ += abs(matrix[i][j])

                absolute = min(absolute, abs(matrix[i][j]))

                if matrix[i][j] < 0:
                    nega_count += 1
        
        if nega_count % 2 != 0:
            summ -= 2 * absolute

        return summ
class Solution(object):
    def numMagicSquaresInside(self, grid):
        
        def check(matrix):
            setto = set()
            for row in matrix:
                for col in row:
                    if col in setto:
                        return False
                    elif col > 9 or col == 0:
                        return False
                    setto.add(col)
            val = sum(matrix[0])
            if val != sum(matrix[1]) or val != sum(matrix[2]):
                return False
            
            for j in range(3):
                summe = 0
                for i in range(3):
                    summe += matrix[i][j]
                
                if summe != val:
                    return False
            
            dia1 = matrix[0][0] + matrix[1][1] + matrix[2][2]
            dia2 = matrix[2][0] + matrix[1][1] + matrix[0][2]
            if dia1 != val or dia2 != val:
                return False
            
            return True
        
        res = 0
        rows = len(grid)
        cols = len(grid[0])
        if rows < 3 or cols < 3:
            return res
        
        for i in range(rows - 2):
            for j in range(cols - 2):
                matri = [grid[i][j:j+3], grid[i+1][j:j+3], grid[i+2][j:j+3]]
                if check(matri):
                    res += 1
            
        return res
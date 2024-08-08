class Solution(object):
    def spiralMatrixIII(self, rows, cols, rStart, cStart):
        res = [[rStart, cStart]]
        x, y = rStart, cStart
        multip = 1
        
        while len(res) != rows * cols:
            for j in range(y + 1, y + 1 + multip):
                if 0 <= j and j < cols and x < rows and 0 <= x:
                    res.append([x, j])
                tmp = j
            y = tmp
            
            for i in range(x + 1, x + 1 + multip):
                if i < rows and 0 <= i and y < cols and 0 <= y:
                    res.append([i, y])
                tmp = i
            x = tmp
            multip += 1

            for j in range(y-1, y - 1 - multip, -1):
                if 0 <= j and j < cols and x < rows and 0 <= x:
                    res.append([x, j])
                tmp = j
            y = tmp

            for i in range(x-1, x - 1 - multip, - 1):
                if i < rows and 0 <= i and y < cols and 0 <= y:
                    res.append([i, y])
                tmp = i
            x = tmp
            multip += 1
        return res
        
class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1:
            return s

        res = [[] for _ in range(numRows)]
        i = 0
        direction = 1
        for c in s:
            if i == 0 and direction == -1:
                direction = 1
            elif i == numRows - 1 and direction == 1:
                direction = -1
            
            res[i].append(c)
            i += direction
        
        return "".join("".join(row) for row in res)
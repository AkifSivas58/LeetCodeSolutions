class Solution:
    def rotateTheBox(self, box: List[List[str]]) -> List[List[str]]:
        m = len(box)
        n = len(box[0])
        new_box = [[0] * m for _ in range(n)]

        for i in range(m):
            for j in range(n):
                new_box[j][m-1-i] = box[i][j]

        for i in range(n-1, -1, -1):
            for j in range(m):
                if new_box[i][j] == ".":
                    for k in range(i-1, -1, -1):
                        if new_box[k][j] == "#":
                            new_box[k][j] = "."
                            new_box[i][j] = "#"
                            break
                        elif new_box[k][j] == "*":
                            break
        
        return new_box

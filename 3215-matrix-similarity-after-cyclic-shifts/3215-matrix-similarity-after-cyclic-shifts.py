class Solution:
    def areSimilar(self, mat: List[List[int]], k: int) -> bool:
        m = len(mat)
        n = len(mat[0])
        k = k % n
        tmp = [row[:] for row in mat]
    
        for i in range(m):
            if i % 2 == 0:
                mat[i] = mat[i][k:] + mat[i][:k]
            else:
                mat[i] = mat[i][-k:] + mat[i][:-k]

        return tmp == mat
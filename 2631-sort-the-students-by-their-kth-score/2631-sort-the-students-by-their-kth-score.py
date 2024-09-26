class Solution:
    def sortTheStudents(self, score: List[List[int]], k: int) -> List[List[int]]:
        m = len(score)
        n = len(score[0])
        
        for i in range(m):
            maxi = 0
            ind = 0
            for j in range(i, m):
                if score[j][k] > maxi:
                    maxi = score[j][k]
                    ind = j
            score[i], score[ind] = score[ind], score[i]
        
        return score



        

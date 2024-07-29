class Solution(object):
    def numTeams(self, rating):
        res = 0
        for j in range(len(rating)):
            left_smaller = 0
            left_greater = 0
            right_smaller = 0
            right_greater = 0

            for i in range(j):
                if rating[i] < rating[j]:
                    left_smaller += 1
                else:
                    left_greater += 1
                
            for k in range(j+1, len(rating)):
                if rating[j] < rating[k]:
                    right_greater += 1
                else:
                    right_smaller += 1
            
            res += left_smaller * right_greater
            res += left_greater * right_smaller

        return res
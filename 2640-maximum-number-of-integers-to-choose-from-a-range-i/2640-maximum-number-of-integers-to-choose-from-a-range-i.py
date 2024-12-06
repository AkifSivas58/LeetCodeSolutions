class Solution:
    def maxCount(self, banned: List[int], n: int, maxSum: int) -> int:
        cur_sum = 0
        ban = set(banned)
        res = 0
        for i in range(1, n + 1):
            if i not in ban:
                cur_sum += i

                if cur_sum > maxSum:
                    break
                
                res += 1
        
        return res
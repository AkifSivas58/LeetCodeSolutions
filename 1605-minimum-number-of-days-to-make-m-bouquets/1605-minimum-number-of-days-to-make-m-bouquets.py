class Solution(object):
    def minDays(self, bloomDay, m, k):
        n = len(bloomDay)
        if m * k > n:
            return -1
        def helper(days):
            bloomed = 0
            bouqets = 0
            for i in range(n):
                if bloomDay[i] <= days:
                    bloomed += 1
                    if bloomed == k:
                        bloomed = 0
                        bouqets += 1
                else:
                    bloomed = 0
            
            if bouqets < m:
                return False

            return True

        low = min(bloomDay)
        high = max(bloomDay)
        while low != high:
            mid = (low+high) // 2
            if helper(mid):
                high = mid
            else:
                low = mid + 1
        
        return low
        
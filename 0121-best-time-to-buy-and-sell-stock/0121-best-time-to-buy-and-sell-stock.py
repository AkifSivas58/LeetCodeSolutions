class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        dp = [0] * n
        res = 0
        mini = prices[0]
        for i in range(1, n):
            res = max(res, prices[i] - mini)
            mini = min(mini, prices[i])
        
        
        return res
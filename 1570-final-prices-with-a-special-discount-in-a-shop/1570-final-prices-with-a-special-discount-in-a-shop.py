class Solution:
    def finalPrices(self, prices: List[int]) -> List[int]:
        answer = []
        for i in range(len(prices)):
            found = False
            for j in range(i+1, len(prices)):
                if prices[i] >= prices[j]:
                    answer.append(prices[i] - prices[j])
                    found = True
                    break

            if not found:
                answer.append(prices[i])
        
        return answer
                    
class Solution(object):
    def bagOfTokensScore(self, tokens, power):
        tokens.sort()
        l = 0
        r = len(tokens) - 1
        score = 0
        maxScore = 0
        while l <= r:
            if tokens[l] <= power and tokens[l] < tokens[r]:
                score += 1
                power -= tokens[l]
                l += 1
                maxScore = max(maxScore, score)
            elif tokens[r] <= power:
                score += 1
                power -= tokens[r]
                r -= 1
                maxScore = max(maxScore, score)

            elif score >= 1:

                if tokens[l] == tokens[r]:
                    break

                score -= 1
                if tokens[l] > tokens[r]:
                    power += tokens[l]
                    l += 1
                else:
                    power += tokens[r]
                    r -= 1
            else:
                l += 1
            
        return maxScore
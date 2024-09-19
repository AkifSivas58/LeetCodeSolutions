class Solution:
    def diffWaysToCompute(self, expression: str) -> List[int]:
        memo = {}

        def recur(exp):
            if exp in memo:
                return memo[exp]

            if exp.isdigit():
                return [int(exp)]
            
            res = []
            for i in range(len(exp)):
                if exp[i] in "+-*":
                    left_res = recur(exp[:i])
                    right_res = recur(exp[i+1:])
                
                    for left in left_res:
                        for right in right_res:
                            if exp[i] == "+":
                                res.append(left + right)
                            elif exp[i] == "-":
                                res.append(left-right)
                            elif exp[i] == "*":
                                res.append(left*right)
                            
            memo[exp] = res
            return res

        return recur(expression)
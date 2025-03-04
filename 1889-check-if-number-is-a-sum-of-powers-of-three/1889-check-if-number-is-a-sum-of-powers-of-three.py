class Solution:
    def checkPowersOfThree(self, n: int) -> bool:
        
        def backtrack(power, num):
            if num == 0:
                return True

            if num < 3 ** power:
                return False

            add = backtrack(power + 1, num - 3 ** power)
            skip = backtrack(power + 1, num)

            return add or skip
        
        return backtrack(0, n)
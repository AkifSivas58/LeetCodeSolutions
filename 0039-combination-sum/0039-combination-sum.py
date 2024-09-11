class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []

        def backtrack(curr, combi, ind):
            if curr == target:
                res.append(list(combi))
                return
            elif curr > target:
                return

            for i in range(ind, len(candidates)):
                combi.append(candidates[i])
                backtrack(curr + candidates[i], combi, i)
                combi.pop()

        backtrack(0, [], 0)
        return res
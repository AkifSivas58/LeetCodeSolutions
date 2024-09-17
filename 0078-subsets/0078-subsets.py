class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        def backtrack(start, curr_sub):
            res.append(curr_sub[:])
            for i in range(start, len(nums)):
                curr_sub.append(nums[i])
                backtrack(i+1, curr_sub)
                curr_sub.pop()
            
        backtrack(0, [])
        return res
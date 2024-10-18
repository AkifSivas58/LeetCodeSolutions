class Solution:
    def countMaxOrSubsets(self, nums: List[int]) -> int:
        def subsets(numbers):
            if numbers == []:
                return [[]]
            x = subsets(numbers[1:])
            return x + [[numbers[0]] + y for y in x]
        
        subs = subsets(nums)

        maxi = 0
        for sub in subs:
            if not sub:
                continue
            
            n = len(sub)
            orr = sub[0]
            for i in range(1, n):
                orr = orr | sub[i]
            
            maxi = max(maxi, orr)
        
        res = 0
        for sub in subs:
            if not sub:
                continue
            
            n = len(sub)
            orr = sub[0]
            for i in range(1, n):
                orr = orr | sub[i]
            
            if orr == maxi:
                res += 1
            
        return res
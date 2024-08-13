class Solution(object):
    def combinationSum2(self, candidates, target):
        candidates.sort()
        res = []
        def helper(combi, summ, start):
                if summ == target:
                    res.append(combi[:]) 
                    return
                
                for i in range(start, len(candidates)):
            
                    if i > start and candidates[i] == candidates[i - 1]:
                        continue
                    
                    if summ + candidates[i] > target:
                        break 
                    
                    combi.append(candidates[i])
                    helper(combi, summ + candidates[i], i + 1)
                    combi.pop() 
        
        helper([], 0, 0)
        return res
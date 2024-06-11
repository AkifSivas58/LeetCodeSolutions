from collections import defaultdict 
class Solution(object):
    def relativeSortArray(self, arr1, arr2):
        hashi = defaultdict(int)
        for num in arr1:
            hashi[num] += 1
        
        res = []
        for num in arr2:
            res.extend([num] * hashi[num])
        
        notinarr2 = []
        for num in arr1:
            if num not in arr2:
                notinarr2.append(num)
        notinarr2.sort()
        res.extend(notinarr2)
        return res
        
        
        
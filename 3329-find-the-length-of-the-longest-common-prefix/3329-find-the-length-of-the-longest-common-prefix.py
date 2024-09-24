class Solution:
    def longestCommonPrefix(self, arr1: List[int], arr2: List[int]) -> int:
        prefs = set()
        for num in arr1:
            st = str(num)
            for i in range(len(st)):
                prefs.add(st[:i+1])
        maxi = 0
        for num in arr2:
            st = str(num)
            for i in range(len(st)):
                if st[:i+1] in prefs:
                    maxi = max(maxi, i+1)
        
        return maxi
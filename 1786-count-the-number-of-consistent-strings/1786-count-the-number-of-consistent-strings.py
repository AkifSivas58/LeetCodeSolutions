class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        res = 0
        for word in words:
            valid = False
            for c in word:
                if c not in allowed:
                    valid = False
                    break
                else:
                    valid = True
            
            if valid:
                res += 1
        
        return res

class Solution:
    def addSpaces(self, s: str, spaces: List[int]) -> str:
        new_str = ""
        ind = 0
        for i in range(len(s)):
            if ind < len(spaces) and i == spaces[ind]:
                new_str = new_str + " "
                ind += 1
            
            new_str = new_str + s[i]
        
        return new_str
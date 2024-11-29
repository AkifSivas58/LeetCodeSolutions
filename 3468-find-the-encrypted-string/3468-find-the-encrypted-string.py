class Solution:
    def getEncryptedString(self, s: str, k: int) -> str:
        new_s = ""
        for i in range(len(s)):
            new_s += s[(i+k) % len(s)]
        
        return new_s
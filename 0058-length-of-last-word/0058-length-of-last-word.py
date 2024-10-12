class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        s.lstrip()
        s.rstrip()
        words = s.split()
        return len(words[-1])
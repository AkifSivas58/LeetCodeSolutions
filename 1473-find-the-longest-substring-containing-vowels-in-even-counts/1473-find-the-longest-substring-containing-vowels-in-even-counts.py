class Solution:
    def findTheLongestSubstring(self, s: str) -> int:
        mask = 0
        maxi = 0
        vowels = {'a': 0, 'e': 1, 'i': 2, 'o': 3, 'u': 4}
        first_occurrence = {0: -1}
        
        for i, c in enumerate(s):
            if c in vowels:
                bit_pos = vowels[c]
                mask ^= (1 << bit_pos)

            if mask in first_occurrence:
                maxi = max(maxi, i - first_occurrence[mask])
            else:
                first_occurrence[mask] = i
        
        return maxi
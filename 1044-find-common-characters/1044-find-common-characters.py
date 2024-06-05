class Solution(object):
    def commonChars(self, words):
        chars = {}
        for ch in words[0]:
            if ch not in chars:
                chars[ch] = 1
            else:
                chars[ch] += 1

        for word in words[1:]:
            current_count = {}
            for ch in word:
                if ch in current_count:
                    current_count[ch] += 1
                else:
                    current_count[ch] = 1
                
            for ch in chars.keys():
                if ch in current_count:
                    chars[ch] = min(chars[ch], current_count[ch])
                else:
                    chars[ch] = 0

        res = []
        for ch in chars:
            res.extend([ch] * chars[ch])
        
        return res
                    
        
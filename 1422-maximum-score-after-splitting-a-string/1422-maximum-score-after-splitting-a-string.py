class Solution(object):
    def maxScore(self, s):
        ones_pref = []
        curr = 0
        for i in range(len(s)):
            if s[i] == "1":
                curr += 1
                ones_pref.append(curr)
            else:
                ones_pref.append(curr)

        zer_count = 0
        maxi = 0
        for i in range(len(s)-1):
            if s[i] == "0":
                zer_count += 1
            
            maxi = max(maxi, zer_count + ones_pref[-1] - ones_pref[i])
        
        return maxi
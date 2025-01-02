class Solution:
    def vowelStrings(self, words: List[str], queries: List[List[int]]) -> List[int]:
        pref = [0] * len(words)
        vowels = ['a', 'e', 'i', 'o', 'u']

        if words[0][0] in vowels and words[0][-1] in vowels:
            pref[0] = 1

        for i in range(1, len(words)):
            pref[i] = pref[i-1]

            if words[i][0] in vowels and words[i][-1] in vowels:
                pref[i] += 1
        
        ans = []
        for l, r in queries:
            if l == 0:
                ans.append(pref[r])
            else:
                ans.append(pref[r] - pref[l-1])

        return ans
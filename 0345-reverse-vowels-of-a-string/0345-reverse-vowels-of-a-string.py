class Solution:
    def reverseVowels(self, s: str) -> str:
        vowels = "AaEeIiOoUu"
        n = len(s)
        l, r = 0, n-1
        st = []
        for c in s:
            st.append(c)

        while l < r:
            if st[l] in vowels and not st[r] in vowels:
                r -= 1
            elif not st[l] in vowels and st[r] in vowels:
                l += 1
            elif st[l] in vowels and st[r] in vowels:
                st[l], st[r] = st[r], st[l]
                l += 1
                r -= 1
            else:
                l += 1
                r -= 1
        
        return "".join(st)
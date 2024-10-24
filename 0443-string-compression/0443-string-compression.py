class Solution:
    def compress(self, chars: List[str]) -> int:
        l, r = 0, 0
        lenn = 0
        while l < len(chars):
            lenn = 1
            while  l+lenn < len(chars) and chars[l] == chars[l+lenn]:
                lenn += 1
            chars[r] = chars[l]
            r += 1
            if lenn > 1:
                st = str(lenn)
                chars[r:r+len(st)] = list(st)
                r += len(st)
            l += lenn
        return r

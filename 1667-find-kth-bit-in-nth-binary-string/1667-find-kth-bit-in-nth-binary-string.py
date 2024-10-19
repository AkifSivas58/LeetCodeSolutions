class Solution:
    def findKthBit(self, n: int, k: int) -> str:
        s = "0"
        def invert_and_reverse(st):
            inverted = []
            for c in st:
                if c == "0":
                    inverted.append("1")
                else:
                    inverted.append("0")
            
            return "".join(reversed(inverted))
        
        for _ in range(n):
            s = s + "1" + invert_and_reverse(s)
        
        return s[k-1]
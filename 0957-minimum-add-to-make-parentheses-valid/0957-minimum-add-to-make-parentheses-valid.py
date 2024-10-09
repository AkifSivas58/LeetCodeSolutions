class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        close_need = 0
        open_need = 0
        for c in s:
            if c == "(":
                close_need += 1
            else:
                if close_need > 0:
                    close_need -= 1
                else:
                    open_need += 1

        return open_need + close_need
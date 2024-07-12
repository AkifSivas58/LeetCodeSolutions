class Solution(object):
    def maximumGain(self, s, x, y):
        res = 0
        if x > y:
            primary = "ab"
            secondary = "ba"
            prim = x
            secon = y
        else:
            primary ="ba"
            secondary = "ab"
            prim = y
            secon = x
        
        stack = [s[0]]
        for c in s[1:]:
            if stack and stack[-1] == primary[0] and c == primary[1]:
                res += prim
                stack.pop()
            else:
                stack.append(c)
        
        new_string = "".join(stack)
        stack = []
        for c in new_string:
            if stack and stack[-1] == secondary[0] and c == secondary[1]:
                res += secon
                stack.pop()
            else:
                stack.append(c)
        
        return res
            
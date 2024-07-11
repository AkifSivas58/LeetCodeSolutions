class Solution(object):
    def reverseParentheses(self, s):
        stack = []
        for c in s:
            if c == ")":
                popped = stack.pop()
                pops = []
                while popped != "(":
                    pops.append(popped)
                    popped = stack.pop()
                    
                stack.extend(pops)
            else:
                stack.append(c)
        
        ress = "".join(map(str, stack))
        return ress
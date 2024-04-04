class Solution(object):
    def maxDepth(self, s):
        stack = []
        max_depth = 0
        current_depth = 0
        for c in s:
            if c == "(":
                current_depth += 1
                stack.append(c)
            elif c == ")":
                current_depth -= 1
                stack.pop()
            
            max_depth = max(max_depth, current_depth)
        
        return max_depth
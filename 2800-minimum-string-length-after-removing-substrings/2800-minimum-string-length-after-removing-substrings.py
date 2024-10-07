class Solution:
    def minLength(self, s: str) -> int:
        n = len(s)
        stack = [s[0]]
        for i in range(1, n):
            if stack and stack[-1] == "A" and s[i] == "B":
                stack.pop()
            elif stack and stack[-1] == "C" and s[i] == "D":
                stack.pop()
            else:
                stack.append(s[i])
        
        return len(stack)

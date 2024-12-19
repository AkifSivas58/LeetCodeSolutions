class Solution:
    def maxChunksToSorted(self, arr: List[int]) -> int:
        stack = []
        n = len(arr)

        for i in range(n):
            if not stack or arr[i] > stack[-1]:
                stack.append(arr[i])
            else:
                maxElement = stack[-1]

                while stack and arr[i] < stack[-1]:
                    stack.pop()
                
                stack.append(maxElement)
        
        return len(stack)
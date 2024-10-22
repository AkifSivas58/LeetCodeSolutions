# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def kthLargestLevelSum(self, root: Optional[TreeNode], k: int) -> int:
        sums = []
        depth = 1
        queue = deque()
        queue.append(root)
        
        while queue:
            level_sum = 0
            level_size = len(queue)
            
            for _ in range(level_size):
                curr = queue.popleft()
                level_sum += curr.val

                if curr.right:
                    queue.append(curr.right)

                if curr.left:
                    queue.append(curr.left)
            
            sums.append(level_sum)

        sums.sort()
        if k <= len(sums):
            return sums[-k]
        return -1

        
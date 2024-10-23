# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def replaceValueInTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        queue = deque()
        head = root
        queue.append(root)
        level_sums = []

        while queue:
            summ = 0
            level_size = len(queue)
            
            for _ in range(level_size):
                node = queue.popleft()
                summ += node.val

                if node.left:
                    queue.append(node.left)
                
                if node.right:
                    queue.append(node.right)
            
            level_sums.append(summ)
        
        queue.append(root)
        root.val = 0
        ind = 1
        while queue:
            level_size = len(queue)

            for _ in range(level_size):
                node = queue.popleft()
                sibling = 0
                if node.left:
                    sibling += node.left.val
                
                if node.right:
                    sibling += node.right.val
                
                if node.left:
                    node.left.val = level_sums[ind] - sibling
                    queue.append(node.left)
                
                if node.right:
                    node.right.val = level_sums[ind] - sibling
                    queue.append(node.right)
            
            ind += 1
        
        return root


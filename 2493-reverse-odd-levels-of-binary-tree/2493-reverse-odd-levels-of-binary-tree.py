# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def reverseOddLevels(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        level = 0
        q = [root]

        while q:
            size = len(q)
            curr_nodes = []

            for _ in range(size):
                node = q.pop(0)
                curr_nodes.append(node)

                if node.left:
                    q.append(node.left)

                if node.right:
                    q.append(node.right)

            if level % 2 == 1:
                l, r = 0, len(curr_nodes) - 1

                while l < r:
                    tmp = curr_nodes[l].val
                    curr_nodes[l].val = curr_nodes[r].val
                    curr_nodes[r].val = tmp
                    l+=1
                    r-=1
            level += 1

        return root 
                
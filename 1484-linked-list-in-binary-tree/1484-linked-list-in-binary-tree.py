
class Solution(object):
    def isSubPath(self, head, root):
        if not head:
            return True

        if not root:
            return False

        def recur(l, t):
            if not l:
                return True
            
            if not t:
                return False

            if l.val != t.val:
                return False

            return recur(l.next, t.right) or recur(l.next, t.left)
        
        def dfs(t):
            if not t:
                return False
            
            if recur(head, t):
                return True
            
            return dfs(t.left) or dfs(t.right)
        
        return dfs(root)
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        def rec(node):
            if node is None or node.next is None:
                return node
            
            start = rec(node.next)
            
            node.next.next = node
            node.next = None

            return start
        
        return rec(head)

            

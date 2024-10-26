class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        stack = []

        while head and head.next:
            stack.append(head)
            head = head.next

        while stack:
            node = stack.pop()
            node.next.next = node
            node.next = None


        return head

            

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def mergeNodes(self, head):
        fast = head
        slow = head
        summ = 0
        while fast.next is not None:
            fast = fast.next
            summ += fast.val

            if fast.val == 0:
                slow.val = summ
                if fast.next is not None:
                    slow = slow.next
                    summ = 0

        slow.next = None
        return head

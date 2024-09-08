# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def splitListToParts(self, head, k):
        n = 0
        tmp = head
        while tmp:
            n += 1
            tmp = tmp.next
        
        res = []
        elements = n // k
        additional = n % k

        current = head
        for _ in range(k):
            part_head = current
            part_size = elements + (1 if additional > 0 else 0)

            if additional > 0:
                additional -= 1
            
            for _ in range(part_size - 1):
                if current:
                    current = current.next
            
            if current:
                next_part = current.next
                current.next = None
                current = next_part
            
            res.append(part_head)
        
        return res
        
        
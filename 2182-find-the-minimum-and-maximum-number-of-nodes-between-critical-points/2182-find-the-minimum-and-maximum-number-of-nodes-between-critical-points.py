# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def nodesBetweenCriticalPoints(self, head):
        res = [-1, -1]
        mini = float('inf')
        prev = head.val
        dist = float('inf')
        count = 0
        ind = 1
        first = 0
        last = 0
        while head.next:
            head = head.next
            ind += 1
            if count > 0:
                dist += 1
            
            if head.next is not None:
                if (prev < head.val and head.next.val < head.val) or (prev > head.val and head.next.val > head.val):
                    count += 1
                    mini = min(mini, dist)
                    dist = 0
                    if count == 1:
                        first = ind
                    last = ind
            prev = head.val
            
        if count < 2:
            return res
        else:
            return [mini, last - first]

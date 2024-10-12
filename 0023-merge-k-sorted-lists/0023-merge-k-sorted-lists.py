# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
import heapq
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        k = len(lists)
        tmp = ListNode()
        curr = tmp

        pq = []
        heapq.heapify(pq)
        for i, l in enumerate(lists):
            if l:
                heapq.heappush(pq, (l.val, i, l))
        print(pq)
        while pq:
            val, i, l = heapq.heappop(pq)
            curr.next = l
            l = l.next
            curr = curr.next
            if l:
                heapq.heappush(pq, (l.val, i, l))
        
        return tmp.next
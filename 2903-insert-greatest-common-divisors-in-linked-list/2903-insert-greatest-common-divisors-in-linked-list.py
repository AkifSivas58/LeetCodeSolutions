# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def insertGreatestCommonDivisors(self, head):
        def gcd(a, b):
            # Find minimum of a and b
            result = min(a, b)

            while result:
                if a % result == 0 and b % result == 0:
                    break
                result -= 1

            # Return the gcd of a and b
            return result
        
        curr = head
        while curr.next:
            res = gcd(curr.val, curr.next.val)
            new = ListNode(res)
            new.next = curr.next
            curr.next = new
            curr = curr.next.next
        
        return head
        
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:

        last = head

        for i in range(n):
            last = last.next
        
        if not last:
            return head.next

        first = head
        last = last.next

        while last:
            first = first.next
            last = last.next

        tmp = first.next.next
        first.next = tmp
        return head

        

        
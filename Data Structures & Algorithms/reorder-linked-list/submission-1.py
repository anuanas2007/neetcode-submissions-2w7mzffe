# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        prev = {}
        temp = head
        while temp:
            if temp.next:
                prev[temp.next] = temp
            else:
                prev[head] = temp
            temp = temp.next
        
        le = len(prev) // 2

        l = prev[head]
        rec = head
        for i in range(le):
            dum = rec.next
            rec.next = l
            rec = rec.next
            rec.next = dum
            rec = rec.next
            l = prev[l]
        rec.next = None


            
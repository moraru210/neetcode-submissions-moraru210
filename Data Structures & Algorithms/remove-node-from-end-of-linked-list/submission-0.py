# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        N = 0
        curr = head
        while curr:
            N += 1
            curr = curr.next
        
        remove_i = N - n
        if remove_i == 0:
            return head.next

        curr = head
        curr_next = head.next
        for i in range(remove_i-1):
            curr = curr_next
            curr_next = curr_next.next
        
        curr.next = curr_next.next

        return head
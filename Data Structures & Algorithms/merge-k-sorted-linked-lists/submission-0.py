# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class NodeCompare:
    def __init__(self, val=0, node=None):
        self.val = val
        self.node = node

    def __lt__(self, other):
        return self.val < other.val 

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        heap = []
        
        for curr in lists:
            while curr:
                heapq.heappush(heap, NodeCompare(curr.val, curr))
                curr = curr.next

        dummy = ListNode()
        new_list = ListNode()
        dummy.next = new_list
        while heap:
            new_node = heapq.heappop(heap)
            new_list.next = new_node.node
            new_list = new_list.next 

        return dummy.next.next       
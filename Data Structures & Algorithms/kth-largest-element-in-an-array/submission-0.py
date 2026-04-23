class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        max_heap = [-x for x in nums]
        heapq.heapify(max_heap)

        kth = 0
        for i in range(k):
            kth = heapq.heappop(max_heap)

        return kth * -1
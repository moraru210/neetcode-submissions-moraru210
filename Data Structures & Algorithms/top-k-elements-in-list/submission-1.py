class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        max_heap = []
        count = Counter(nums)

        for n, freq in count.items():
            heapq.heappush(max_heap, (-freq, n))

        res = []
        while len(res) < k and max_heap:
            _, n = heapq.heappop(max_heap)
            res.append(n)

        return res
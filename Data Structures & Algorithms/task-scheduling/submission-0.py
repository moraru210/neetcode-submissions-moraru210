class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        count = Counter(tasks)
        max_heap = [-n for n in count.values()]
        heapq.heapify(max_heap)
        print(max_heap)

        q = deque()
        min_cycles = 0
        while max_heap or q:
            min_cycles += 1

            if not max_heap:
                time = q[0][1]
            else:
                cnt = 1 + heapq.heappop(max_heap)
                if cnt:
                    q.append([cnt, min_cycles + n])
            if q and q[0][1] == min_cycles:
                heapq.heappush(max_heap, q.popleft()[0])

        return min_cycles
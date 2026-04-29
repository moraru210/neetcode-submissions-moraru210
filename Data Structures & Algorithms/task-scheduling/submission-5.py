class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        count = Counter(tasks)
        max_heap = [-n for n in count.values()]
        heapq.heapify(max_heap)

        queue = deque() # store (remaining_count, next_available)
        time = 0
        while max_heap or queue:
            time += 1
            if not max_heap:
                time = queue[0][1]
            else:
                freq = 1 + heapq.heappop(max_heap)
                if freq:
                    queue.append([freq, time + n])
            if queue and queue[0][1] == time:
                heapq.heappush(max_heap, queue.popleft()[0])

        return time

            
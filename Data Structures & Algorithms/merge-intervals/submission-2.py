class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        print(intervals)
        res = [intervals[0]]
        for curr in intervals[1:]:
            last = res[-1]
            if curr[0] <= last[1]:
                res[-1][0] = min(curr[0], last[0])
                res[-1][1] = max(curr[1], last[1])
            else:
                res.append(curr)

        return res
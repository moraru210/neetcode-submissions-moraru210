class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        left = max(weights)
        right = sum(weights)
        res = right

        def satisfy(cap):
            ships = 1
            currCap = cap
            for w in weights:
                if currCap - w < 0:
                    ships += 1
                    if ships > days:
                        return False
                    currCap = cap
                currCap -= w
            return True



        while left <= right:
            mid = (left+right) // 2
            if satisfy(mid):
                res = mid
                right = mid - 1
            else:
                left = mid + 1


        return res
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        res = 0
        curSum = 0
        prefix_sum = {}
        prefix_sum[0] = 1
        for i, n in enumerate(nums):
            curSum += n
            diff = curSum - k
            res += prefix_sum.get(diff, 0)
            prefix_sum[curSum] = 1 + prefix_sum.get(curSum, 0)
        
        return res



        
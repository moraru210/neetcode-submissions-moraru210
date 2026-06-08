class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [float("inf")] * (amount+1)
        # for a in amount:
        #     if a < len(dp):
        #         dp[a] = 1

        dp[0] = 0
        for i in range(len(dp)):
            for a in coins:
                new_ch = a + i
                new_n = dp[i] + 1
                if new_ch < len(dp):
                    dp[new_ch] = min(dp[new_ch], new_n)
        
        return -1 if dp[-1] == float("inf") else dp[-1]
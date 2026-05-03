class Solution:
    def numSquares(self, n: int) -> int:
        dp = [n] * (n+1)
        dp[0] = 0

        for i in range(1, n + 1):
            for s in range(1, i+1):
                square = s*s
                if i - square < 0:
                    break

                dp[i] = min(dp[i], 1 + dp[i - square])

        return dp[n]



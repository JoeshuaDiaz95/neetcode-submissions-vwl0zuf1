class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
    # dp[c] = number of ways to reach current row at column c
        dp = [1] * n

        for _ in range(1, m):
            for c in range(1, n):
                dp[c] += dp[c - 1]

        return dp[-1]
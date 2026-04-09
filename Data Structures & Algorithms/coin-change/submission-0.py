class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        #initializing dp list
        dp = [float('inf')] * (amount + 1)
        #initial condition
        dp[0] = 0


        for x in range(1,amount+1):
            for c in coins:
                if (x-c) >= 0:
                    dp[x] = min(dp[x],dp[x-c]+1)
    
        if dp[amount] == float('inf'):
            return -1
        else:
            return dp[amount]


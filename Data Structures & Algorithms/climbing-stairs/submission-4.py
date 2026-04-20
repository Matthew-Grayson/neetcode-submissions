class Solution:
    def climbStairs(self, n: int) -> int:
        # dynamic programming
        # calculate steps needed for n=1 and n=2
        # increment calculation by one up until n
        if n <= 2:
            return n
        dp = [0] * (n + 1)
        dp[1] = 1
        dp[2] = 2
        for i in range(3, n + 1):
            dp[i] = dp[i - 1] + dp[i - 2]
        print(dp)
        
        return dp[n]

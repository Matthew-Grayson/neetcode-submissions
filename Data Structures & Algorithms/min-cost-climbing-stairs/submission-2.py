class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        # dynamic programming (top-down)

        memo = [-1] * len(cost)

        # return memo[i] if already calculated;
        # otherwise calculate, save, and return memo[i]
        def dfs(i):
            if i >= len(cost):
                return 0
            
            if memo[i] != -1:
                return memo[i]

            memo[i] = cost[i] + min(dfs(i + 1), dfs(i + 2))

            return memo[i]

        return min(dfs(0), dfs(1))
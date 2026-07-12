class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # time: O(n)
        # sliding window
        # space: O(1)
        # edge: len(prices) < 2
        if len(prices) <= 1:
            return 0
        profit = 0
        left, right = 0, 1

        while right < len(prices):
            profit = max(profit, prices[right] - prices[left])
            if prices[right] < prices[left]:
                left = right
            right += 1

        return profit
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        #  sliding window O(n) time / O(1) space
        left = 0
        right = 1
        profit = 0
        while right < len(prices):
            if prices[right] < prices[left]:
                left = right
            else:
                profit = max(profit, prices[right] - prices[left])
            right += 1

        return profit

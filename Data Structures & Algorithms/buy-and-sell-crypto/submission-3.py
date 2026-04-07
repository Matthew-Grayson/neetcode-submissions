class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        left = 0
        right = 1
        result = 0

        while right < len(prices):
            if prices[right] < prices[left] and right < len(prices) - 1:
                left = right
                right = left + 1
            result = max(result, prices[right] - prices[left])
            right += 1
            
        return result
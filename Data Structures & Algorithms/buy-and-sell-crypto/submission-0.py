# Algorithm
#    sliding window
# 
# Constaints
#    1 <= prices.length <= 100
#    0 <= prices[i] <= 100
# 
# Edge Cases
#   prices.length = 1

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxProfit = 0
        minPrice = prices[0]
        buyPoint, sellPoint = 0, 1
        while sellPoint < len(prices):
            maxProfit = max(maxProfit, prices[sellPoint] - prices[buyPoint])
            if minPrice > prices[sellPoint]:
                minPrice = prices[sellPoint]
                buyPoint = sellPoint
                sellPoint = buyPoint + 1
            else:
                sellPoint += 1
        return maxProfit
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy_price = prices[0]

        profit = 0

        for sell_price in prices:
            if sell_price < buy_price:
                buy_price = sell_price
            else:
                profit = max(profit, sell_price - buy_price)

        return profit
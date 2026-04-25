class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # find the best profit
        min_price = prices[0]
        max_profit = 0 
        for i, price in enumerate(prices[1:]):
            min_price = min(price, min_price)
            max_profit = max(max_profit, price - min_price)
        return max_profit
            

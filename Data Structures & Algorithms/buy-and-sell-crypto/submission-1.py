class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        min_value_until_now = prices[0]
        for i in range(1, len(prices)):
            if min_value_until_now > prices[i]:
                min_value_until_now = prices[i]
                continue 
            max_profit = max(max_profit, prices[i] - min_value_until_now)
        return max_profit 

            

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy_at = prices[0]
        max_profit = 0

        for i in range(1, len(prices)):

            # Can I buy cheaper today?
            if prices[i] < buy_at:
                buy_at = prices[i]

            # If I sell today, what's my profit?
            profit = prices[i] - buy_at

            # Remember the best profit
            max_profit = max(max_profit, profit)

        return max_profit
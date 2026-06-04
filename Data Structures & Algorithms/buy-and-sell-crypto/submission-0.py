class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy_at = prices[0]
        result = 0

        for i in range(1, len(prices)):
            if prices[i] < buy_at:
                buy_at = prices[i]
            else:
                result = max(result, prices[i] - buy_at)

        return result
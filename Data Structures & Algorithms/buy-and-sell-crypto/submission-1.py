class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max = 0
        for i in range (len(prices)):
            for k in range (i+1, len (prices)):
                if prices[k] - prices[i] > max:
                    max = prices[k] - prices[i]
        return max
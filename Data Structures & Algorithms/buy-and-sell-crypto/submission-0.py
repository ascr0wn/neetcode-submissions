class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max = 0
        for buyindex in range(len(prices) - 1):
            for sellindex in range(buyindex+1, len(prices)):
                if prices[sellindex] - prices[buyindex] > max:
                    max = prices[sellindex] - prices[buyindex]
        return max

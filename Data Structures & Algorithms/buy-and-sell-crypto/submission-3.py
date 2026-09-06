class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buyindex, sellindex, max = 0,0,0
        for currentindex in range(len(prices)):
            if prices[currentindex] < prices[buyindex]:
                buyindex = currentindex
                sellindex = currentindex + 1
                if sellindex == len(prices):
                    return max
                max = prices[sellindex] - prices[buyindex] if prices[sellindex] - prices[buyindex] > max else max
            elif prices[currentindex] > prices[sellindex]:
                sellindex = currentindex
                max = prices[sellindex] - prices[buyindex] if prices[sellindex] - prices[buyindex] > max else max
        return max
// https://leetcode.com/problems/best-time-to-buy-and-sell-stock

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxNum = 0
        minNum = math.inf
        for i in range(len(prices)):
            if prices[i] - minNum > maxNum:
                maxNum = prices[i] - minNum
            if prices[i] < minNum:
                minNum = prices[i]
        return maxNum
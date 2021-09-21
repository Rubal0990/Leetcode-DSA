class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxProfit = 0
        minsofar = prices[0]
        
        for i in range(len(prices)):
            minsofar = min(minsofar, prices[i])
            profit = prices[i] - minsofar
            maxProfit = max(maxProfit, profit)
        
        return maxProfit

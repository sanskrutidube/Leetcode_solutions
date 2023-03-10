class Solution:
    def maxProfit(self,prices):
        left = 0 
        right = 1 
        max_profit = 0
        while right < len(prices):
            currentProfit = prices[right] - prices[left] 
            if prices[left] < prices[right]:
                max_profit =max(currentProfit,max_profit)
            else:
                left = right
            right += 1
        return max_profit

---------------------------------------------------------------------

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices:
            return 0
        maxProfit = 0
        minPurchase = prices[0]
        for i in range(1, len(prices)):
            maxProfit = max(maxProfit, prices[i] - minPurchase)
            minPurchase = min(minPurchase, prices[i])
        return maxProfit







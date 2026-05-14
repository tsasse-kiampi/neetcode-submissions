class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxGain = 0

        left, right = 0, 1
        while right < len(prices):
            if prices[left] < prices[right]:
                maxGain = max(maxGain, prices[right] - prices[left])
                left, right = left, right + 1
            
            else: 
                maxGain = max(maxGain, prices[right] - prices[left])
                left, right = right, right + 1

        return maxGain        



        
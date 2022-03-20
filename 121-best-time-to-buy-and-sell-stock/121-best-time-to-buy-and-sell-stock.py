class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxDiff = 0
        currMin = math.inf
        
        for price in prices:
            if price < currMin:
                currMin = price
            else:
                maxDiff = max(maxDiff, price - currMin)
                
        return maxDiff
        
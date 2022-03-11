import math
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        largestDiff = 0
        minSoFar = math.inf
        
        for price in prices:
            if price < minSoFar:
                minSoFar = price
            else:
                largestDiff = max(largestDiff, price - minSoFar)
                
        return largestDiff
        
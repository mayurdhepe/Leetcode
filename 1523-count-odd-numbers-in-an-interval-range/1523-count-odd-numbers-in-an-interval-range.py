class Solution:
    def countOdds(self, low: int, high: int) -> int:
        numRange = high - low + 1
        if numRange % 2 == 0 or low % 2 == 0:
            return numRange//2
        
        return numRange//2 + 1
            
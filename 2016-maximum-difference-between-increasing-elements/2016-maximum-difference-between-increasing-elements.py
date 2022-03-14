import math
class Solution:
    def maximumDifference(self, nums: List[int]) -> int:
        currMin = math.inf
        maxDiff = -1
        for i in range(len(nums)):
            currMin = min(currMin, nums[i])
            maxDiff = max(maxDiff, nums[i] - currMin)
        
        if maxDiff == 0:
            return -1
        
        return maxDiff
            
            
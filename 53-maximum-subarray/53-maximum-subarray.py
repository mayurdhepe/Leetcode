import math
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxSum = -math.inf
        currSubArraySum = 0
        for num in nums:
            currSubArraySum += num   
            maxSum = max(maxSum, currSubArraySum)
            
            if currSubArraySum < 0:
                currSubArraySum = 0
            
        return maxSum
import math
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxSum = -math.inf
        subArrSum = 0
        for i in range(len(nums)):
            subArrSum += nums[i]
            maxSum = max(maxSum, subArrSum)
            if subArrSum < 0:
                subArrSum = 0
            
        return maxSum
            
        
class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        n = len(nums)
        summ = 0 
        
        for i in range(n):
            summ += nums[i]
        
        preSum = 0
        for i in range(n):
            if preSum == (summ - nums[i] - preSum):
                return i
            
            preSum += nums[i]
            
        return -1
        
        
class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        # arrSum = 0
        # for i in range(len(nums)):
        #     arrSum += nums[i]
        arrSum = sum(nums)
        
        leftSum = 0
        for i, num in enumerate(nums):
            if leftSum == arrSum - leftSum - num:
                return i
            
            leftSum += num
            
        return -1
                
        
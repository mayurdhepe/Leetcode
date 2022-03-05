class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
       
        index = 0  
        j = 0
        
        while j < len(nums):
            if nums[j] != 0:
                nums[index] = nums[j]
                index += 1
            j += 1 

        while index < len(nums):
            nums[index] = 0
            index += 1
            
        return nums
        
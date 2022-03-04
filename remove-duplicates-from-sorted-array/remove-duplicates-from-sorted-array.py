class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        # we start from one since first number is always going to be unique
        index = 1  
        j = 0
        # traverse the array till len of array - 1
        while j < len(nums)-1:
            if nums[j] != nums[j+1]:
                # place the 2nd number at index pos
                nums[index] = nums[j+1]
                index += 1
            j += 1 
            
        return index
            
            
        
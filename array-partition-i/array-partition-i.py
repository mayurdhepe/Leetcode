class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        nums.sort()
        
        li = nums[::2]
        return sum(li)
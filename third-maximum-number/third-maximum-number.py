class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        
        if len(nums) == 2:
            return max(nums[0], nums[1])
            
        numsSet = list(set(nums))
        
        if len(numsSet) == 1:
            return numsSet[0]
        
        if len(numsSet) == 2:
            return max(numsSet[0], numsSet[1])
        
        sortedSet = sorted(numsSet, reverse=True)
        return sortedSet[2]
        
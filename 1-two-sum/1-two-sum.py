class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        myDict = {}
        n = len(nums)
        for i in range(n):
            comp = target - nums[i]
            if (comp in myDict):
                return [i, myDict[comp]]
                
            myDict[nums[i]] = i
                
                
        
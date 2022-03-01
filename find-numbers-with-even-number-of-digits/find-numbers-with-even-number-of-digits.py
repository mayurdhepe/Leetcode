class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        ans = 0
        for i in range(len(nums)):
            num = nums[i]
            digitCount = 0
            while num > 0:
                num = num // 10
                digitCount += 1
                
            if digitCount % 2 == 0:
                ans += 1
                
        return ans
                
            
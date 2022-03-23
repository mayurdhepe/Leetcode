class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        n = len(numbers)
        l, r = 0, n-1
        res = []
        while l<r:
            twoSum = numbers[l] + numbers[r]
            if twoSum > target:
                r -= 1
            elif twoSum < target:
                l += 1
            else:
                res.append(l+1)
                res.append(r+1)
                l += 1
                while numbers[l] == numbers[l-1] and l < r:
                    l += 1
        
        return res
                
        
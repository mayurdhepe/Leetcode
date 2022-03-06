class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        newHeights = heights.copy()
        newHeights.sort()
        ans = 0
        for i in range(len(heights)):
            if heights[i] != newHeights[i]:
                ans += 1
                
        return ans
                
        
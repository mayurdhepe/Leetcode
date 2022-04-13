class Solution:
    def longestPalindrome(self, s: str) -> int:
        res = 0
        
        count = {}
        for c in s:
            count[c] = count.get(c, 0) + 1
            
        oddFound = False
        
        for ch, cnt in count.items():
            if cnt % 2 == 0:
                res += cnt
            else:
                oddFound = True
                res += cnt - 1
        
        if oddFound:
            res += 1
            
        return res
            
        
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        count = {}
        for c in s:
            count[c] = count.get(c, 0) + 1
        
        print(count)
        for c in t:
            if c in count and count[c] >= 1:
                count[c] -= 1
            else:
                return False
        
        print(count)
        if sum(list(count.values())) == 0:
            return True
            
        
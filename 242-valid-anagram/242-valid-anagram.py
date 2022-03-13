class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        hashMap = {}
        for ch in s:
            hashMap[ch] = hashMap.get(ch, 0) + 1
           
        for ch in t:
            if hashMap.get(ch):
                hashMap[ch] -= 1
            else:
                return False
            
        if sum(list(hashMap.values())) == 0:
	        return True
            
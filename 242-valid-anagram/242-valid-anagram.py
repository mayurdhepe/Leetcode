from collections import Counter
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        hashS = Counter(s)
        hashT = Counter(t)
        
        return hashS == hashT
        
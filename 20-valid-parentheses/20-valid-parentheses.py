class Solution:
    def isValid(self, s: str) -> bool:
        dic = { "(": ")",
               "{": "}",
               "[": "]" 
              }
        stack = []
        
        for c in s:
            if c in dic.keys():
                stack.append(c)
            else:
                if not stack:
                    return False
                
                top = stack.pop()
               
                if dic[top] != c:
                    return False
                
        return not stack
                
        
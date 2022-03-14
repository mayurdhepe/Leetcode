class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        
        for i in range(len(s)):
            if s[i] != "]":
                stack.append(s[i])
            else:
                substr = ""
                # pop everything until we reach a opening bracket
                while stack[-1] != "[":
                    substr = stack.pop() + substr
                
                # pop the bracket
                stack.pop()
                
                # pop the digits
                k = ""
                while stack and stack[-1].isdigit():
                    k = stack.pop() + k
                
                stack.append(int(k) * substr)
            
        return "".join(stack)
                
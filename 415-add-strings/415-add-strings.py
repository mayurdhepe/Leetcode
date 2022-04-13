class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        res = []
        ans = ""
        carry = 0
        
        p1, p2 = len(num1)-1, len(num2)-1
        
        while p1 >= 0 or p2 >= 0:
            n1 = ord(num1[p1]) - ord('0') if p1 >= 0 else 0
            n2 = ord(num2[p2]) - ord('0') if p2 >= 0 else 0
            
            value = (carry + n1 + n2) % 10
            carry = (carry + n1 + n2) // 10
            res.append(value)
            
            p1 -= 1
            p2 -= 1
        
        if carry > 0:
            res.append(carry)
            
        for n in res[::-1]:
            ans += str(n)
            
        return ans
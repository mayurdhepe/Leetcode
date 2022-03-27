class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        product = 1
        summ = 0
        while n>0:
            digit = n % 10
            product = product * digit
            summ = summ + digit
            n = n//10
        
        return (product - summ)
            
        
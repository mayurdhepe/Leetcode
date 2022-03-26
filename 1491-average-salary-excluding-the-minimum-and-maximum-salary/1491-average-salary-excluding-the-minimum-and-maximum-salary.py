class Solution:
    def average(self, salary: List[int]) -> float:
        salary.sort()
        n = len(salary)
        avg = 0
        summ = 0
        for i in range(1, n-1):
            summ += salary[i]
        
        return summ / (n-2)
        
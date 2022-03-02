class Solution:
    def duplicateZeros(self, arr: List[int]) -> None:
        """
        Do not return anything, modify arr in-place instead.
        """
        n = len(arr)
        # n1 - increased arr length after adding zeroes
        n1 = len(arr)
        zeroes = 0
        for i in range(n):
            if arr[i] == 0:
                zeroes += 1
                
        n1 = n + zeroes
        i = n-1
        j = n1 - 1
        
        while (i != j):
            self.insert(arr, i, j)
            j -= 1
            
            if (arr[i] == 0):
                self.insert(arr, i, j)
                j -= 1
            
            i -= 1
            
    
    def insert(self, arr, i, j):
        if (j < len(arr)):
            arr[j] = arr[i]
                
        
                
class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:
        arrSet = set()
        for i in range(len(arr)):
            if arr[i]*2 in arrSet or (arr[i] % 2 == 0 and arr[i]/2 in arrSet):
                return True
            arrSet.add(arr[i])
            
        return False
        
class MedianFinder:

    def __init__(self):
        self.numlist = []
        
    def addNum(self, num: int) -> None:
        self.numlist.append(num)

    def findMedian(self) -> float:
        print(self.numlist.sort())
        n = int(len(self.numlist))
        if n%2 == 0:
            return (self.numlist[n // 2 - 1] + self.numlist[n // 2]) / 2
        
        return self.numlist[n//2] 


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()
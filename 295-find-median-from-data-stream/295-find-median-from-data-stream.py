import heapq
class MedianFinder:

    def __init__(self):
        # min heap to store upper order elements
        self.minHeap = []
        # max heap to store lower order elements
        self.maxHeap = []
        # count to add elements alternatively
        self.count = 0

    def addNum(self, num: int) -> None:
        if self.count % 2 == 0:
            # add in max heap (lower order)
            heapq.heappush(self.maxHeap, -num)
        else:
            # add in min heap (upper order)
            heapq.heappush(self.minHeap, num)
        
        self.count += 1
        if self.count > 1:
            if -self.maxHeap[0] > self.minHeap[0]:
                low = heapq.heappop(self.maxHeap)
                high = heapq.heappop(self.minHeap)
                #swap
                heapq.heappush(self.minHeap, -low)
                heapq.heappush(self.maxHeap, -high)
            
            
    def findMedian(self) -> float:
        if self.count % 2 == 0:
            return (-self.maxHeap[0] + self.minHeap[0])/2
        
        return -self.maxHeap[0]


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()
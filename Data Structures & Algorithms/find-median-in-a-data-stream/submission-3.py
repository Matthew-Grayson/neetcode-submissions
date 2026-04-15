class MedianFinder:
    # maintain maxHeap (left) and minHeap (right)
    # rebalance if len diff > 1 after insert

    def __init__(self):
        self.left = []
        self.right = []
        

    def addNum(self, num: int) -> None:
        if self.left and num > self.left[0]:
            heapq.heappush(self.right, num)
        else:
            heapq.heappush_max(self.left, num)

        diff = len(self.left) - len(self.right)
        if diff < -1:
            val = heapq.heappop(self.right)
            heapq.heappush_max(self.left, val)
        elif diff > 1:
            val = heapq.heappop_max(self.left)
            heapq.heappush(self.right, val)



    def findMedian(self) -> float:
        diff = len(self.left) - len(self.right)
        if diff > 0:
            return self.left[0]
        if diff < 0:
            return self.right[0]
        return (self.left[0] + self.right[0]) / 2
        
        
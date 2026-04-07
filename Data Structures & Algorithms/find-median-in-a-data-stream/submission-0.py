class MedianFinder:

    def __init__(self):
        self.left_heap = []
        self.right_heap = []

    def addNum(self, num: int) -> None:
        if self.left_heap and num > self.left_heap[0]:
            heapq.heappush(self.right_heap, num)
        else:
            heapq.heappush_max(self.left_heap, num)
        diff = len(self.left_heap) - len(self.right_heap)
        if diff > 1:
            temp = heapq.heappop_max(self.left_heap)
            heapq.heappush(self.right_heap, temp)
        if diff < -1:
            temp = heapq.heappop(self.right_heap)
            heapq.heappush_max(self.left_heap, temp)

    def findMedian(self) -> float:
        diff = len(self.left_heap) - len(self.right_heap)
        if diff > 0:
            return self.left_heap[0]
        if diff < 0:
            return self.right_heap[0]
        return (self.left_heap[0] + self.right_heap[0]) / 2
        
        
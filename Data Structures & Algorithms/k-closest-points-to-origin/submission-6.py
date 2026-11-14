class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:       
        minheap = []
        res = []

        for x, y in points:
            distance = x ** 2 + y ** 2
            heapq.heappush(minheap, (distance, [x, y]))
        
        for _ in range(k):
            coords = heapq.heappop(minheap)[1]
            res.append(coords)
        
        return res
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:       
        minheap = []
        res = []

        for coords in points:
            distance = coords[0] ** 2 + coords[1] ** 2
            heapq.heappush(minheap, tuple((distance, coords)))
        
        for _ in range(k):
            coords = heapq.heappop(minheap)[1]
            res.append(coords)
        
        return res
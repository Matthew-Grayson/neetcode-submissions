class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        # is it possible to avoid floats since we don't return the sqrt?
        # convert points to tuple (distance, [x, y])
        # store tuples in min_heap
        # return coordinates from k popped tuples

        minheap = []
        res = []

        for coords in points:
            distance = math.sqrt(coords[0] ** 2 + coords[1] ** 2)
            heapq.heappush(minheap, tuple((distance, coords)))
        
        for _ in range(k):
            coords = heapq.heappop(minheap)[1]
            res.append(coords)
        
        return res
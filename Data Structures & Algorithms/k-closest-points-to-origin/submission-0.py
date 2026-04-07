class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        # use heap to sort distances
        # use dictionary to store / lookup associated coords

        minheap = []
        res = []

        for x, y in points:
            dist = x ** 2 + y ** 2
            heapq.heappush(minheap, [dist, x, y])

        while len(res) < k:
            dist, x, y = heapq.heappop(minheap)
            res.append([x, y])
        
        return res
        

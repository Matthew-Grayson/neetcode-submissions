class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        # minheap or maxheap
        # skip sqrt calc; only need relative dist
        maxheap = []
        for x, y in points:
            dist = x**2 + y**2
            heapq.heappush_max(maxheap, (dist, x, y))
            if len(maxheap) > k:
                heapq.heappop_max(maxheap)

        res = []
        for i in range(k):
            dist, x, y = heapq.heappop_max(maxheap)
            res.append([x, y])
        
        return res
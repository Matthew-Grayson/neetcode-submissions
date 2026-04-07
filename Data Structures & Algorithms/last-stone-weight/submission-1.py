class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        maxheap = [-stone for stone in stones]
        heapq.heapify(maxheap)
        while len(maxheap) > 1:
            diff = heapq.heappop(maxheap) - heapq.heappop(maxheap)
            if diff:
                heapq.heappush(maxheap, diff)
                
        if maxheap:
            return -maxheap[0]
        else:
            return 0
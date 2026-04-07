class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        heapq.heapify_max(stones)

        while len(stones) > 1:
            k1 = heapq.heappop_max(stones)
            k2 = heapq.heappop_max(stones)
            if k1 > k2:
                heapq.heappush_max(stones, k1 - k2)
        
        return stones[0] if stones else 0
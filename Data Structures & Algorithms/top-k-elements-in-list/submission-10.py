class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # count nums and store counts as dict {num: count}
        # convert to tuple (count, num) and store in maxheap
        counts = defaultdict(int)
        maxheap = []
        res = []

        for num in nums:
            counts[num] += 1

   

        for num, count in counts.items():
            heapq.heappush_max(maxheap, (count, num))

        for i in range(k):
            res.append(heapq.heappop_max(maxheap)[1])

        return res
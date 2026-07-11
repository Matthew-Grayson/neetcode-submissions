class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # generate dictionary of counts (num: count)
        # multiple nums can have same count
        # convert to tuple (count, value)
        # add to maxHeap

        counts = defaultdict(int)
        maxHeap = []
        res = []
        for num in nums:
            counts[num] += 1

        for num, count in counts.items():
            heapq.heappush_max(maxHeap, (count, num))

        while k > 0:
            res.append(heapq.heappop_max(maxHeap)[1])
            k -= 1

        return res


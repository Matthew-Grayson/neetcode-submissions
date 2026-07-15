class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = defaultdict(int)
        bucket = [[] for i in range(len(nums) + 1)]
        res = []

        for num in nums:
            counts[num] += 1
        
        for num, count in counts.items():
            bucket[count].append(num)

        for i in range(len(bucket) - 1, 0, -1):
            for count in bucket[i]:
                res.append(count)
                if len(res) == k:
                    return res
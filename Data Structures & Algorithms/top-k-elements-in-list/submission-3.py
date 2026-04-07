class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = defaultdict(int)
        bucket = [[] for i in range(len(nums) + 1)]
        res = []
        for num in nums:
            counts[num] += 1
        for num, count in counts.items():
            bucket[count].append(num)
        print(counts)
        print(bucket)

        for i in range(len(bucket) - 1, -1, -1):
            for num in bucket[i]:
                res.append(num)
                k -= 1
                if k == 0:
                    return res
        return res
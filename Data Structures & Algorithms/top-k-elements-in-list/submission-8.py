class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = defaultdict(int)
        freq = [[] for i in range(len(nums) + 1)]
        res = []

        for num in nums:
            counts[num] += 1

        for num, count in counts.items():
            freq[count].append(num)

        while len(res) < k:
            top = freq.pop()
            for num in top:
                res.append(num)

        return res
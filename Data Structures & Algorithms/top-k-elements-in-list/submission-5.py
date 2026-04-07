class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # store counts in dictionary with form `num: count`
        # move counts to bucket where index corresponds to count
        # read from last index of bucket until k numbers are retrieved
        bucket = [[] for x in range(len(nums) + 1)]
        counts = defaultdict(int)
        
        for num in nums:
            counts[num] += 1
        for num, count in counts.items():
            bucket[count].append(num)
        
        res = []
        for i in range(len(bucket) - 1, 0, -1):
            for num in bucket[i]:
                res.append(num)
                if len(res) == k:
                    return res
        return res
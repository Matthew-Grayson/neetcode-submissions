class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # First count occurence of each number
        # place numbers in bucket with index matching count
        # use bucket of lists to account for dupes
        # return last k results in bucket

        counts = defaultdict(int)
        
        for num in nums:
            counts[num] += 1
        print(counts)
        bucket = [[] for i in range(len(nums) + 1)]

        for num, count in counts.items():
            bucket[count].append(num)
        print(bucket)
        res = []

        for i in range(len(bucket) - 1, 0, -1):
            for count in bucket[i]:
                res.append(count)
                if len(res) == k:
                    return res


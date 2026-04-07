class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = defaultdict(list)
        for s in strs:
            counts = [0] * 26
            for c in s:
                code = ord(c) - ord("a")
                counts[code] += 1
            groups[tuple(counts)].append(s)
        return list(groups.values())
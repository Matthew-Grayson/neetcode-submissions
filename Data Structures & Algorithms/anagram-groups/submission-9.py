class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # dictionary of lists
        # key is a count of each letter (tuple)
        groups = defaultdict(list)

        for s in strs:
            count = [0] * 26
            for c in s:
                ordC = ord(c) - ord("a")
                count[ordC] += 1
            groups[tuple(count)].append(s)

        return list(groups.values())
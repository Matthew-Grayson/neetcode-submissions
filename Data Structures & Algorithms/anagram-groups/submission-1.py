class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = dict()
        for s in strs:
            sSort = "".join(sorted(s))
            if sSort in groups:
                groups[sSort].append(s)
            else:
                groups[sSort] = [s]
            
        return list(groups.values())
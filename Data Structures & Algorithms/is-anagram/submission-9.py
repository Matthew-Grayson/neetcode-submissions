class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # count characters in each string and compare
        if len(t) != len(s):
            return False
        
        sCount = defaultdict(int)
        tCount = defaultdict(int)

        for i in range(len(s)):
            sCount[s[i]] += 1
            tCount[t[i]] += 1

        return sCount == tCount

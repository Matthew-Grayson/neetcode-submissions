class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # count letter distribution in each string
        # store count as lists 
        # return True if counts equal else False
        if len(s) != len(t):
            return False
        count_s = defaultdict(int)
        count_t = defaultdict(int)
        for i in range(len(s)):
            count_s[s[i]] += 1
            count_t[t[i]] += 1
        return count_s == count_t
            
        
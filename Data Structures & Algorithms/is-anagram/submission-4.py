class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # iterate through both strings 
        # store count of each letter in each string as dictionaries
        # return True if counts match else False
        if len(s) != len(t):
            return False
        count_s = defaultdict(int)
        count_t = defaultdict(int)
        
        for i in range(len(s)):
            count_s[s[i]] += 1
            count_t[t[i]] += 1

        return count_s == count_t
        
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        
        s1_freq = [0] * 26

        for c in s1:
            s1_freq[ord(c) - ord('a')] += 1
        
        l = 0
        r = len(s1)

        while r <= len(s2):
            sub_str = s2[l:r]

            freq = [0] * 26

            for c in sub_str:
                freq[ord(c) - ord('a')] += 1

            if s1_freq == freq:
                return True
            
            l += 1
            r += 1
        return False


        
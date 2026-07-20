class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        # count chars in s1
        # iterate s2 count using sliding window
        # if s2 count for a char > s1 count, left += 1 until s2 count <= s1 count
        left = 0
        counts1, counts2 = {}, {}

        for c in s1:
            counts1[c] = counts1.get(c, 0) + 1
            
        for c in s2:
            counts2[c] = counts2.get(c, 0) + 1

            if c not in counts1:
                while counts2[c] > 0:
                    counts2[s2[left]] -= 1
                    left += 1
                counts2.pop(c, None)
            elif counts2[c] > counts1[c]:
                 while counts2[c] > counts1[c]:
                    counts2[s2[left]] -= 1
                    left += 1
            if counts1 == counts2:
                return True

        return False
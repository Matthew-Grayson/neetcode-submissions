class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False

        counts1, counts2 = [0] * 26, [0] * 26

        for i in range(len(s1)):
            c1 = ord(s1[i]) - ord("a")
            c2 = ord(s2[i]) - ord("a")
            counts1[c1] += 1
            counts2[c2] += 1

        left, right = 0, len(s1)

        while right < len(s2):
            if counts1 == counts2:
                return True
            cLeft = ord(s2[left]) - ord("a")
            cRight = ord(s2[right]) - ord("a")
            counts2[cLeft] -= 1
            counts2[cRight] += 1
            left += 1
            right += 1
        
        return counts1 == counts2
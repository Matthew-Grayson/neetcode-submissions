class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        counts = defaultdict(int)
        res = 0
        freqMax = 0
        left = 0
        
        for right in range(len(s)):
            counts[s[right]] += 1
            freqMax = max(freqMax, counts[s[right]])

            while (right - left + 1) - freqMax > k:
                counts[s[left]] -= 1
                left += 1
            
            res = max(res, right - left + 1)
            
        return res

class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        longest = 0
        left, right = 0, 0
        subCounts = defaultdict(int)

        while right < len(s):
            subCounts[s[right]] += 1
            freqMax = max(subCounts.values())
            while (right - left + 1 - freqMax) > k:
                subCounts[s[left]] -= 1
                left += 1
            longest = max(longest, right - left + 1)
            right += 1

        return longest
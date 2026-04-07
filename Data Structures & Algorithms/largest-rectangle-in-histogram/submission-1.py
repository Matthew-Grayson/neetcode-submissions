class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        # stack of pairs with height and index

        out = 0

        stack = []
        for i in range(len(heights)):
            area = heights[i]
            j = i - 1
            while j >= 0 and heights[j] >= heights[i]:
                area += heights[i]
                j -= 1
            j = i + 1
            while j < len(heights) and heights[j] >= heights[i]:
                area += heights[i]
                j += 1
            out = max(out, area)

        return out

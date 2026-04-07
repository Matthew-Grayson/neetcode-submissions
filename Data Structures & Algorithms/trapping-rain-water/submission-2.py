class Solution:
    def trap(self, height: List[int]) -> int:
        prefix = [[] for i in range(len(height))]
        postfix = [[] for i in range(len(height))]
        lmax = rmax = 0
        area = 0
        
        for i in range(len(height)):
            lmax = max(lmax, height[i])
            prefix[i] = lmax
        
        for i in range(len(height) - 1, -1, -1):
            rmax = max(rmax, height[i])
            postfix[i] = rmax

        for i in range(len(height)):
            area += min(prefix[i], postfix[i]) - height[i]
        print(prefix, postfix)
        return area

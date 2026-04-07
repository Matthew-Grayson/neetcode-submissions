class Solution:
    def trap(self, height: List[int]) -> int:
        left = 0
        right = len(height) - 1
        lmax = height[left]
        rmax = height[right]
        vol = 0

        while left <= right:
            if lmax < rmax:
                vol += max(0, min(lmax, rmax) - height[left])
                print("left++; lmax: ", lmax, "height[left]: ", height[left], "vol: ", vol)
                left += 1
                lmax = max(lmax, height[left])

            else:
                vol += max(0, min(lmax, rmax) - height[right])
                print("right--; rmax: ", rmax, "height[right]: ", height[right], "vol: ", vol)
                right -= 1
                rmax = max(rmax, height[right])

        return vol
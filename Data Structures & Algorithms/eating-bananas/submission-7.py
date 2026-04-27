class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # calculate hours needed to finish all piles for a given rate
        # check rates between 1 and max(piles) inclusive
        # use binary search to minimize number of values to check
        left = 1
        right = max(piles)

        while left < right:
            rate = (left + right) // 2
            hours = 0
            for pile in piles:
                hours += -(-pile // rate) # double negative for int ceil div
            if hours > h: # rate too low
                left = rate + 1
            else:
                right = rate
        return left
        
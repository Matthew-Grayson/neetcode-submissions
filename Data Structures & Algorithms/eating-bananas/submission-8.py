class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # binary search
        # left, right = 1, max(piles)
        # calculate hours needed for each k checked
        # pileSize / bananas/hour = hours needed to eat pile\

        left, right = 1, max(piles)

        while left < right:
            rate = left + (right - left) // 2
            hours = 0
            for pile in piles:
                hours += -(-pile // rate)

            if hours > h: # rate is too slow
                left = rate + 1

            else:
                right = rate

        return left

            
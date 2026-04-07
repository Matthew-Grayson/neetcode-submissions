class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # brute force requires calculating the hours needed for every eating rate
        # from 1 to max(piles) (as left and right bounds)
        # if hours needed > h, eliminate bottom half of search values
        # else eliminate top half (but keep mid value)
        left, right = 1, max(piles)
        while left < right:
            rate = (left + right) // 2
            hours = 0
            for pile in piles:
                hours += math.ceil(pile / rate)
            if hours > h: # too slow
                left = rate + 1
            else:
                right = rate
        return  left
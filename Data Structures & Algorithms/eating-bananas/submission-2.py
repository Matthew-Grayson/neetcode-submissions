class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # formula to calculate hours needed to eat all piles based on bph
        # use binary search (left = 1, right = max(piles))
        left = 1
        right = max(piles)

        while left < right:
            rate = (left + right) // 2
            hours = 0
            for pile in piles:
                hours +=  -(-pile//rate)
            if hours > h: # rate too slow
                left = rate + 1
            else: # rate is fast enough but can possibly be slower
                right = rate
        
        return right

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:

        left, right = 1, max(piles)
        
        while left < right:
            rate = (left + right) // 2
            hours = 0
            for pile in piles:
                hours += -(-pile // rate)
            if hours > h: # rate too slow
                left = rate + 1
            else:
                right = rate
            
        return left

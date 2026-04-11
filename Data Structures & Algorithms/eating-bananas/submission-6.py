class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # binary search of rate: leftbound = 1; rightbound = max(piles)
        # calculate hours needed for each rate
        # iterate through piles and keep running total of hours for each pile
        # rate / pile = hours (ceiling division)

        left = 1
        right = max(piles)

        while left < right:
            rate = (left + right) // 2
            hours = 0
            for pile in piles:
                hours += -(-pile // rate)
            print("rate: ", rate, "hours: ", hours)
            if hours > h: # too slow
                left = rate + 1
            else: 
                right = rate

        return right

class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        pair =  [(x, v) for x, v in zip(position, speed)]

        pair.sort(reverse=True)
        stack = []
        for x, v in pair:
            stack.append((target - x) / v)
            if len(stack) >= 2 and stack[-1] <= stack[-2]:
                stack.pop()

        return len(stack)
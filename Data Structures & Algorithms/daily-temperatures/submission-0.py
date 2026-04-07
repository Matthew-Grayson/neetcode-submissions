class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        # reversed list as stack
        out =  [0] * len(temperatures)
        stack = []

        for idx, temp in enumerate(temperatures):
            while stack and temp > stack[-1][0]:
                stemp, sidx = stack.pop()
                out[sidx] = idx - sidx
            stack.append([temp, idx])
        return out
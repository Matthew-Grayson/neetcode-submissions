class Solution:
    def climbStairs(self, n: int) -> int:
        if n <= 2:
            return n
            
        key =  [0] * (n + 1)
        key[1] = 1
        key[2] = 2

        for i in range(3, n + 1):
            key[i] = key[i - 1] + key[i - 2]

        return key[n]
    
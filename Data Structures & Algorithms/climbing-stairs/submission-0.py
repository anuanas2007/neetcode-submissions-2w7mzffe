class Solution:
    def climbStairs(self, n: int) -> int:
        if n <= 2:
            return n
        np = [0] * (n+1)
        np[1] = 1
        np[2] = 2

        for i in range(3, n+1):
            np[i] = np[i-1] + np[i-2]
        
        return np[n]
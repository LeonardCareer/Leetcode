class Solution:
    def climbStairs(self, n: int) -> int:
        if n <= 1:
            return 1
        last = 1
        now = 1
        for i in range(1, n):
            last, now = now, last + now
        
        return now

    def climbStairs2(self, n: int) -> int:
        return round(1 / pow(5, 0.5) * pow((1 + pow(5, 0.5)) / 2, n + 1) - 1 / pow(5, 0.5) * pow((1 - pow(5, 0.5)) / 2, n + 1))

temp = Solution()
print(temp.climbStairs2(2))
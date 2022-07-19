class Solution:
    def candy(self, ratings: list[int]) -> int:
        result = [1] * len(ratings)

        for i in range(1, len(ratings)):
            if ratings[i] > ratings[i - 1]:
                result[i] = result[i - 1] + 1

        print(result)
        
        for i in range(len(ratings) - 2, -1, -1):
            if ratings[i] > ratings[i + 1]:
                result[i] = max(result[i + 1] + 1, result[i])

        print(result)
        
        return sum(result)

    def candy2(self, ratings: list[int]) -> int:
        up = down = peak = 0
        result = 1
        for i in range(1, len(ratings)):
            if ratings[i] > ratings[i - 1]:
                up += 1
                peak = up
                down = 0
                result += up + 1
            elif ratings[i] == ratings[i - 1]:
                up = down = peak = 0
                result += 1
            else:
                down += 1
                up = 0
                result += down
                if peak < down:
                    result += 1
        return result


temp = Solution()
ratings = [1,3,4,5,2]
print(temp.candy(ratings))
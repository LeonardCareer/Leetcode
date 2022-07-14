class Solution:
    def plusOne(self, digits: list[int]) -> list[int]:
        result = []
        for i in range(len(digits) - 1, -1, -1):
            num = (digits[i] + 1) % 10
            res = (digits[i] + 1) // 10
            result = [num] + result
            
            if res == 0:
                result = digits[: i] + result
                break

        if result[0] == 0:
            result = [1] + result

        return result

temp = Solution()
print(temp.plusOne([9 ,9 ,9 ,9]))
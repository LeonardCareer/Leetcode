class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        result = []
        myNums = [i for i in range(1, n + 1)]

        def getNumbers(number: int, kth:int):
            factorial = 1
            for i in range(1, number):
                factorial *= i
            index = kth // factorial
            kth %= factorial
            currentNumber = str(myNums[index])
            del myNums[index]
            if number != 1:
                return currentNumber + getNumbers(number - 1, kth)
            else:
                return currentNumber
        
        return getNumbers(n, k - 1)

temp = Solution()
n = 3
k = 1
print(temp.getPermutation(n, k))

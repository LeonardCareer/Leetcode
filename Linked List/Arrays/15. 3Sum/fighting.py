class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        myNums = sorted(nums)
        result = []
        for i in range(len(myNums)):
            if i == 0 or myNums[i] != myNums[i - 1]:
                left = i + 1
                right = len(myNums) - 1
                while left < right:
                    answer = myNums[i] + myNums[left] + myNums[right]
                    if answer > 0:
                        right -= 1
                    elif answer < 0:
                        left += 1
                    else:
                        result.append([myNums[i], myNums[left], myNums[right]])
                        left += 1
                        while left < right and myNums[left] == myNums[left - 1]:
                            left += 1
        return result

temp = Solution()
nums = [0,2,2,3,0,1,2,3,-1,-4,2]
print(temp.threeSum(nums))

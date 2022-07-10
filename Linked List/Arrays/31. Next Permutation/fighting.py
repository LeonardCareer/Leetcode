class Solution:
    def nextPermutation(self, nums: list[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        for i in range(len(nums) - 1, 0, -1):
            if nums[i - 1] < nums[i]:
                before = nums[i - 1]
                index = i
                difference = nums[i] - before
                for j in range(i + 1, len(nums)):
                    differenceNew = nums[j] - before
                    if 0 < differenceNew < difference:
                        index = j
                        difference = differenceNew
                nums[i - 1], nums[index] = nums[index], nums[i - 1]
                nums[i :] = sorted(nums[i : ])
                break
        else:
            nums.sort()


temp = Solution()
nums = [1, 3, 2]
temp.nextPermutation(nums)
print(nums)
temp.nextPermutation(nums)
print(nums)
temp.nextPermutation(nums)
print(nums)
temp.nextPermutation(nums)
print(nums)
temp.nextPermutation(nums)
print(nums)
temp.nextPermutation(nums)
print(nums)
temp.nextPermutation(nums)
print(nums)

temp.nextPermutation(nums)
print(nums)
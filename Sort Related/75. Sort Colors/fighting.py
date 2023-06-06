class Solution:
    def sortColors(self, nums: list[int]) -> None:
        count_0 = nums.count(0)
        count_1 = nums.count(1)
        for i in range(len(nums)):
            if i < count_0:
                nums[i] = 0
            elif i < count_0 + count_1:
                nums[i] = 1
            else:
                nums[i] = 2


    def sortColors(self, nums: list[int]) -> None:
        l, r = 0, len(nums) - 1
        i = 0
        while i <= r:
            if nums[i] == 0:
                nums[i], nums[l] = nums[l], nums[i]
                l += 1
            elif nums[i] == 2:
                nums[i], nums[r] = nums[r], nums[i]
                r -= 1
                i -= 1
            i += 1
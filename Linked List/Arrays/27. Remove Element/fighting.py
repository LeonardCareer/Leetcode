class Solution:
    def removeElement(self, nums: list[int], val: int) -> int:
        # for i in range(nums.count(val)):
        #     nums.remove(val)
        # return len(nums)

        index = 0
        for i in range(len(nums)):
            if nums[i] != val:
                nums[index] = nums[i]
                index += 1
        return index

temp = Solution()
nums = [3,2,2,3]
val = 3
print(temp.removeElement(nums, val))
print(nums)


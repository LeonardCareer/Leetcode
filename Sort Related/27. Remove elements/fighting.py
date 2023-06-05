class Solution:
    def removeElement(self, nums: list[int], val: int) -> int:
        next_available = 0
        for i in range(len(nums)):
            if nums[i] != val:
                nums[next_available] = nums[i]
                next_available += 1
        return next_available

test = Solution()
nums = [3,2,2,3]
val = 3
# 2, nums = [2,2,_,_] except
print(test.removeElement(nums, val))
print(nums)

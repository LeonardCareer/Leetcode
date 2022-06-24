class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        if not nums:
            return None

        place = 1
        for i in range(1, len(nums)):
            if nums[i] != nums[i - 1]:
                nums[place] = nums[i]
                place += 1
        
        return place

solution = Solution()
nums = [1, 1, 2]
print(solution.removeDuplicates(nums))
print(nums)

class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        if not nums:
            return None

        count = 1
        place = 1
        for i in range(1, len(nums)):
            if nums[i] != nums[i - 1]:
                nums[place] = nums[i]
                place += 1
                count = 1
            else:
                if count == 1:
                    nums[place] = nums[i]
                    place += 1
                    count = 2
        return place

    def removeDuplicates2(self, nums: list[int]) -> int:
        if not nums:
            return None
        elif len(nums) < 2:
            return len(nums)
        
        place = 2
        for i in range(2, len(nums)):
            if nums[i] != nums[place - 2]:
                nums[place] = nums[i]
                place += 1
        return place

solution = Solution()
nums = [1,1,1,2,2,3]
print(solution.removeDuplicates(nums))
print(nums)
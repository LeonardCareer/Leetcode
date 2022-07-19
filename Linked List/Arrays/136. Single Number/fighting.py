class Solution:
    def singleNumber2(self, nums: list[int]) -> int:
        return sum(nums) * 2 - sum(set(nums))
    
    def singleNumber(self, nums: list[int]) -> int:
        result = 0
        for i in nums:
            result ^= i
        return result
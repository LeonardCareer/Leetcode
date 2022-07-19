class Solution:
    def singleNumber2(self, nums: list[int]) -> int:
        return round((3 * sum(set(nums)) - sum(nums)) / 2)

    def singleNumber(self, nums: list[int]) -> int:
        one = two = three = 0

        for i in nums:
            two |= (one & i)
            one ^= i
            three = (two & one)
            one &= ~three
            two &= ~three
        return one
class Solution:
    def singleNumber(self, nums: list[int]) -> list[int]:
        xor = 0

        for i in nums:
            xor ^= i

        # let x and y is the answer, we need to find 1 bit that x is not equal with y
        # xor is 010100 - xor is 101111, complement

        xor &= -xor

        group1 = 0
        group2 = 0
        for i in nums:
            if i & xor:
                group1 ^= i
            else:
                group2 ^= i
        return [group1, group2]
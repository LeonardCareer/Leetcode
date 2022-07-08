class Solution:
    def longestConsecutive(self, nums: list[int]) -> int:
        mySet = set(nums)
        longest = 0
        for num in mySet:
            if (num - 1) not in mySet:
                length = 1
                while (num + length) in mySet:
                    length += 1
                longest = max(longest, length)
        return longest
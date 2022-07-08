class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        visited = {}
        first = second = None
        for index in range(len(nums)):
            aim = target - nums[index]
            if aim in visited:
                first = visited[aim]
                second = index
                break
            visited[nums[index]] = index

        return [first, second]

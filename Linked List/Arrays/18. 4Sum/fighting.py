# class Solution:
#     def fourSum(self, nums: list[int], target: int) -> list[list[int]]:
#         nums.sort()
#         answer = []
#         for i in range(len(nums)):
#             if i == 0 or nums[i - 1] != nums[i]:
#                 for j in range(i + 1, len(nums)):
#                     if j == i + 1 or nums[j] != nums[j - 1]:
#                         left = j + 1
#                         right = len(nums) - 1
#                         while left < right:
#                             number = nums[i] + nums[j] + nums[left] + nums[right]

#                             if number > target:
#                                 right -= 1
#                             elif number < target:
#                                 left += 1
#                             else:
#                                 answer.append([nums[i], nums[j], nums[left], nums[right]])
#                                 left += 1
#                                 while left < right and nums[left] == nums[left - 1]:
#                                     left += 1
#         return answer

class Solution:
    def fourSum(self, nums: list[int], target: int) -> list[list[int]]:
        nums.sort()
        answer = []
        rest = []
        print(nums)

        def kSum(k: int, target: int, start: int):
            if k != 2:
                for i in range(start, len(nums)):
                    if i == start or nums[i] != nums[i - 1]:
                        rest.append(nums[i])
                        # print(rest, i, start, k, target - nums[i]) 
                        kSum(k - 1, target - nums[i], i + 1)
                        rest.pop()
            else:
                left = start
                right = len(nums) - 1
                while left < right:
                    # print(rest + [nums[left], nums[right]], sum(rest + [nums[left], nums[right]]))
                    if nums[left] + nums[right] < target:
                        left += 1
                    elif nums[left] + nums[right] > target:
                        right -= 1
                    else:
                        answer.append(rest + [nums[left], nums[right]])
                        left += 1
                        while left < right and nums[left - 1] == nums[left]:
                            left += 1
        kSum(4, target, 0)
        return answer


temp = Solution()
nums = [1,0,-1,0,-2,2]
target = 0
print(temp.fourSum(nums, target))
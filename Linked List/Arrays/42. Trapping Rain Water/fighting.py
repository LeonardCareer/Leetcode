# class Solution:
#     def trap(self, height: list[int]) -> int:
#         result = 0
#         indexLeft = indexRight = height.index(max(height))
        
#         left, right = indexLeft - 1, indexRight + 1
#         while left > 0:
#             leftNum = max(height[: indexLeft])
#             while height[left] != leftNum:
#                 left -= 1
#             result += leftNum * (indexLeft - left - 1) - sum(height[left + 1: indexLeft])
#             indexLeft = left
#             left -= 1

#         while right < len(height) - 1:
#             rightNum = max(height[indexRight + 1:])
#             while height[right] != rightNum:
#                 right += 1
#             result += rightNum * (right - indexRight - 1) - sum(height[indexRight + 1: right])
#             indexRight = right
#             right += 1
        
#         return result

# class Solution:
#     def trap(self, height: list[int]) -> int:
#         if max(height) == min(height):
#             return 0
#         result = []
#         for i in range(1, len(height) - 1):
#             maxLeft = max(0, max(height[:i]))
#             maxRight = max(0, max(height[i + 1:]))
#             result.append(max(min(maxLeft, maxRight) - height[i], 0))
#         print(result)
#         return sum(result)

class Solution:
    def trap(self, height: list[int]) -> int:
        left, right = 1, len(height) - 2
        maxLeft, maxRight = height[0], height[-1]
        
        result = 0
        while left <= right:
            if maxLeft < maxRight:
                maxLeft = max(maxLeft, height[left])
                result += maxLeft - height[left]
                left += 1
            else:
                maxRight = max(maxRight, height[right])
                result += maxRight - height[right]
                right -= 1
        return result


temp = Solution()
print(temp.trap([2, 0, 2]))
from functools import cmp_to_key
class Solution:
    def largestNumber(self, nums: list[int]) -> str:
        string_nums = list(map(str, nums))
        result = self.mergeSort(string_nums)
        result = "".join(result)
        while len(result) > 1 and result.startswith("0"):
            result = result[1:]
        return result
    
    def mergeSort(self, nums):
        if len(nums) <= 1:
            return nums
        mid = len(nums) // 2
        left = nums[:mid]
        right = nums[mid:]
        return self.merge(self.mergeSort(left), self.mergeSort(right))

    def merge(self, nums1, nums2):
        result = []
        i = j = 0
        while i < len(nums1) and j < len(nums2):
            if int(nums1[i] + nums2[j]) > int(nums2[j] + nums1[i]):
                result.append(nums1[i])
                i += 1
            else:
                result.append(nums2[j])
                j += 1
        if i != len(nums1):
            result.extend(nums1[i:])
        if j != len(nums2):
            result.extend(nums2[j:])
        return result

    def largestNumber2(self, nums: list[int]) -> str:
        string_nums = list(map(str, nums))
        def compare(n1, n2):
            if n1 + n2 > n2 + n1:
                return -1
            else:
                return 1
        result = "".join(sorted(string_nums, key=cmp_to_key(compare)))
        while len(result) > 1 and result.startswith("0"):
            result = result[1:]
        return result
    

test = Solution()
nums = [3,30,34,5,9]
nums2 = [0, 0, 0, 0]
print(test.largestNumber2(nums2))
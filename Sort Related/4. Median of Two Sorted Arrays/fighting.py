class Solution:
    def findMedianSortedArrays(self, nums1: list[int], nums2: list[int]) -> float:
        total = len(nums1) + len(nums2)

        # O(m + n)
        # def findKthElement(k):
        #     nums1Point, nums2Point = 0, 0
        #     count = 0
        #     while nums1Point < len(nums1) and nums2Point < len(nums2):
        #         if count == k:
        #             return min(nums1[nums1Point], nums2[nums2Point])
        #         if nums1[nums1Point] < nums2[nums2Point]:
        #             nums1Point += 1
        #         else:
        #             nums2Point += 1
        #         count += 1
        #     if nums1Point == len(nums1):
        #         return nums2[k - len(nums1)]
        #     else:
        #         return nums1[k - len(nums2)]
        # if total % 2 == 0:
        #     return (findKthElement(total // 2 - 1) + findKthElement(total // 2)) / 2
        # else:
        #     return float(findKthElement(total // 2))
        
            
        # O(log(m + n)) since nums1 and num2 are sorted
        def findKthElement2(lst1, lst2 ,k):
            if len(lst1) > len(lst2):
                return findKthElement2(lst2, lst1, k)
            
            if len(lst1) == 0:
                return lst2[k - 1]

            if k == 1:
                return min(lst1[0], lst2[0])
            
            mid1 = min(k // 2, len(lst1) - 1)
            mid2 = k - mid1

            if lst1[mid1 - 1] < lst2[mid2 - 1]:
                return findKthElement2(lst1[mid1:], lst2, k - mid1)
            elif lst2[mid2 - 1] < lst1[mid1 - 1]:
                return findKthElement2(lst1, lst2[mid2:], k - mid2)
            else:
                return lst1[mid1]
            
        if total % 2 == 0:
            return (findKthElement2(nums1, nums2, total // 2) + findKthElement2(nums1, nums2, total // 2 + 1)) / 2
        else:
            return float(findKthElement2(nums1, nums2, total // 2 + 1))
        
test = Solution()
nums1 = [1,2]
nums2 = [3]
print(test.findMedianSortedArrays(nums1, nums2))

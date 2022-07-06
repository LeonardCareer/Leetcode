class Solution:
    def findMedianSortedArrays(self, nums1: list[int], nums2: list[int]) -> float:
        total = len(nums1) + len(nums2)
        if total % 2 == 0:
            return (self.findKstNumber(nums1, nums2, total // 2) + self.findKstNumber(nums1, nums2, total // 2 + 1)) / 2
        else:
            return self.findKstNumber(nums1, nums2, total // 2 + 1)

    def findKstNumber(self, nums1: list[int], nums2: list[int], k: int) -> float:
        if len(nums1) > len(nums2):
            return self.findKstNumber(nums2, nums1, k)

        if len(nums1) == 0:
            return nums2[k - 1]

        if k == 1:
            return min(nums1[0], nums2[0])

        mid1 = min(k // 2, len(nums1))
        mid2 = k - mid1

        if nums1[mid1 - 1] < nums2[mid2 - 1]:
            return self.findKstNumber(nums1[mid1:], nums2, k - mid1)
        elif nums1[mid1 - 1] > nums2[mid2 - 1]:
            return self.findKstNumber(nums1, nums2[mid2:], k - mid2)
        else:
            return nums1[mid1 - 1]


nums1 = [1, 2, 3, 4, 5, 6, 7, 8]
nums2 = [1, 2, 3, 4, 5]
temp = Solution()
print(temp.findMedianSortedArrays(nums1, nums2))

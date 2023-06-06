# Average Time Complexity: O(N)
# Worst Case Time Complexity: O(N^2)
# Space Complexity: O(N)

class Solution:
    def findKthLargest(self, nums: list[int], k: int) -> int:
        target = len(nums) - k

        def quickSelect(l, r):
            pivot, p = nums[r], l
            for i in range(l, r):
                if nums[i] <= pivot:
                    nums[p], nums[i] = nums[i], nums[p]
                    p += 1
            nums[p], nums[r] = nums[r], nums[p]
            
            if p > target:
                return quickSelect(l, p - 1)
            elif p < target:
                return quickSelect(p + 1, r)
            else:
                return nums[p]

        return quickSelect(0, len(nums) - 1)

    def findKthLargest2(self, nums: list[int], k: int) -> int:
        pivot = nums[0]
        
        left = [num for num in nums if num < pivot]
        equal = [num for num in nums if num == pivot]
        right = [num for num in nums if num > pivot]
        
        if k <= len(right): return self.findKthLargest(right, k)
        elif len(right) < k <= len(right) + len(equal): return equal[0]
        else: return self.findKthLargest(left, k - len(right) - len(equal))
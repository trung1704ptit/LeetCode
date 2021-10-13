class Solution(object):
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        def quickselect(nums, left, right):
            i, j = left + 1, right 
            while True:
                while i <= j and nums[i] <= nums[left]: i+= 1
                while j >= i and nums[j] >= nums[left]: j-= 1
                if i > j: break
                # swap nums[i], nums[j]
                nums[i], nums[j] = nums[j], nums[i]

            # swap nums[left], nums[j]
            nums[left], nums[j] = nums[j], nums[left]

            return j

        n, k = len(nums), len(nums) - k
        left, right = 0, n - 1

        while left < right:
            i = quickselect(nums, left, right)

            if i < k:
                left = i + 1

            elif i > k:
                right = i - 1

            else: break

        return nums[k]
class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums) - 1  # Initialize binary search boundaries

        while left <= right:
            mid = (left + right) // 2  # Calculate middle index

            if nums[mid] == target:
                return mid  # If target found, return its index
            elif nums[mid] < target:
                left = mid + 1  # Move search range to the right half
            else:
                right = mid - 1  # Move search range to the left half

        # If target is not found, 'left' will be the insert position
        return left
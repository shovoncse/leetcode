class Solution:
    def isMonotonic(self, nums: List[int]) -> bool:
        # Check if the length of the array is 2 or less, in which case it is considered monotonic
        if len(nums) <= 2:
            return True

        # Check the order of the first and last elements to determine the direction
        if nums[0] <= nums[-1]:
            # If non-decreasing order is expected
            for i in range(1, len(nums)):
                # Check if any element is smaller than the previous one
                if nums[i] < nums[i - 1]:
                    return False
        else:
            # If non-increasing order is expected
            for i in range(1, len(nums)):
                # Check if any element is greater than the previous one
                if nums[i] > nums[i - 1]:
                    return False

        # If no inconsistency is found, the array is monotonic
        return True

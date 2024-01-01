class Solution:
    def isMonotonic(self, nums: List[int]) -> bool:
        # Initialize flags for increasing and decreasing to True
        increasing = decreasing = True
            
        # Iterate through the nums starting from index 1
        for i in range(1, len(nums)):
            # Check if the current element is greater than the previous one
            if nums[i] > nums[i - 1]:
                # If yes, set decreasing flag to False (nums is not decreasing)
                decreasing = False
            # Check if the current element is smaller than the previous one
            if nums[i] < nums[i - 1]:
                # If yes, set increasing flag to False (nums is not increasing)
                increasing = False
            
        # Return True if either increasing or decreasing is still True, indicating monotonicity
        return increasing or decreasing


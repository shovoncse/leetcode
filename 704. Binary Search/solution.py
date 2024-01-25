class Solution:
    def search(self, nums: List[int], target: int) -> int:
        

        def rec(nums, target, start, end):
            if start > end:
                return -1
            
            mid  = (start + end) // 2
            
            if nums[mid] == target:
                return mid
            elif target < nums[mid]:
                return rec(nums, target, start, mid - 1)
            else:
                return rec(nums, target, mid + 1, end)
        
        return rec(nums, target, 0, len(nums) - 1)
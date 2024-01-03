class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        indices = {}
        res = []
        for i, cur in enumerate(nums):
            gap = target - cur
            if gap in indices:
                res = [i, indices[gap]]
                break
            indices[cur] = i
        return res
class Solution:
    def findMatrix(self, nums: List[int]) -> List[List[int]]:
        occ = collections.Counter(nums)
        number_rows = max(occ.values())
        
        res = [[] for _ in range(number_rows)]
        
        for num, count in occ.items():
            for i in range(count):
                res[i].append(num)
        
        return res
class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        # O(sqrt(n))
        # for i in range(1, num + 1):
        #     if i * i == num:
        #         return True
        #     if i * i > num:
        #         return False

        # Binary Search
        l, r = 1, num

        while l <= r:
            m = (l + r) // 2

            if m * m == num:
                return True

            if m * m > num:
                r = m - 1
            else:
                l = m + 1

        return False 
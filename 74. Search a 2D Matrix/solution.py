class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        topRow = 0
        bottomRow = len(matrix) - 1

        while topRow <= bottomRow:
            middleRow = (topRow + bottomRow) // 2

            if target > matrix[middleRow][-1]: 
                topRow = middleRow + 1
            elif target < matrix[middleRow][0]:
                bottomRow = middleRow - 1
            else:
                # must in current row
                break
        
        if not (topRow <= bottomRow):
            return False
        
        targetRow = (topRow + bottomRow) // 2

        l = 0
        r = len(matrix[0]) - 1
        while l <= r:
            mid = (l+r) // 2
            if target > matrix[targetRow][mid]:
                l = mid + 1
            elif target < matrix[targetRow][mid]:
                r = mid - 1
            else:
                return True
        
        return False


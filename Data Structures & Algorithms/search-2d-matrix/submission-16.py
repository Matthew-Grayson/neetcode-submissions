class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # duplicates within rows (but not between)
        # return boolean
        # binary search to find row that could contain target
        # binary search to find target in that row

        top = 0
        bot = len(matrix) - 1
        left = 0
        right = len(matrix[0]) - 1

        while top <= bot:
            mid = top + (bot - top) // 2
            row = matrix[mid]
            if row[left] > target:
                bot = mid - 1
            elif row[right] < target:
                top = mid + 1
            else:
                break
        
        if top > bot:
            return False
        
        while left <= right:
            mid = left + (right - left) // 2
            if row[mid] > target:
                right = mid - 1
            elif row[mid] < target:
                left = mid + 1
            else:
                return True
        
        return False


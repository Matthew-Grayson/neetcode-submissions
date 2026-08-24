class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # duplicates within rows (but not between)
        # return boolean
        # binary search to find row that could contain target
        # binary search to find target in that row

        top = 0
        bot = len(matrix) - 1

        while top <= bot:
            mid = top + (bot - top) // 2
            row = matrix[mid]
            if row[0] > target:
                bot = mid - 1
            elif row[len(matrix[0]) - 1] < target:
                top = mid + 1
            else:
                return self.b_search(row, target)
        return False
        

    def b_search(self, nums, target):
        left = 0
        right = len(nums) - 1
        while left <= right:
            mid = left + (right - left) // 2
            if nums[mid] > target:
                right = mid - 1
            elif nums[mid] < target:
                left = mid + 1
            else:
                return True
        return False
        
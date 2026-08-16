func searchMatrix(matrix [][]int, target int) bool {
    top := 0
    bottom := len(matrix) - 1
    left := 0
    right := len(matrix[0]) - 1

    for top <= bottom {
        row := top + (bottom - top) / 2
        if matrix[row][0] > target {
            bottom = row - 1
        } else if matrix[row][right] < target {
            top = row + 1
        } else {
            for left <= right {
                mid := left + (right - left) / 2
                if matrix[row][mid] > target {
                    right = mid - 1
                } else if matrix[row][mid] < target {
                    left = mid + 1
                } else {
                    return true
                }
            }
            return false
        }
    }
    return false
}

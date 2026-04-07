class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = [0] * 9
        cols =  [0] * 9
        squares = [0] * 9

        for row in range(9):
            square_row = (row // 3) * 3
            for col in range(9):
                ch = board[row][col]
                if ch == ".":
                    continue

                square = square_row + (col // 3)
                mask = 1 << ord(ch) - ord("1")
                if (mask & rows[row]) or (mask & cols[col]) or (mask & squares[square]):
                    return False

                rows[row] |= mask
                cols[col] |= mask
                squares[square] |= mask

        return True
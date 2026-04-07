class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = [0] * 9
        cols =  [0] * 9
        squares = [0] * 9

        for row in range(9):
            for col in range(9):
                if board[row][col] == ".":
                    continue

                bit = 1 << ord(board[row][col]) - ord("1")
                if (bit & rows[row]) or (bit & cols[col]) or (bit & squares[(row // 3) * 3 + (col // 3)]):
                    return False

                rows[row] |= bit
                cols[col] |= bit
                squares[(row // 3) * 3 + (col // 3)] |= bit

        return True
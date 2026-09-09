class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:

        rows = len(board)
        cols = len(board[0])

        def dfs(row, col, index):

            # word is completely found
            if index == len(word):
                return True

            # out of bounds
            if row < 0 or row >= rows or col < 0 or col >= cols:
                return False

            # wrong character
            if board[row][col] != word[index]:
                return False

            # save character
            temp = board[row][col]

            # mark as visited
            board[row][col] = "#"

            # search 4 directions
            found = (
                dfs(row + 1, col, index + 1) or
                dfs(row - 1, col, index + 1) or
                dfs(row, col + 1, index + 1) or
                dfs(row, col - 1, index + 1)
            )

            # restore character
            board[row][col] = temp

            return found

        # try every cell as starting point
        for row in range(rows):
            for col in range(cols):
                if dfs(row, col, 0):
                    return True

        return False
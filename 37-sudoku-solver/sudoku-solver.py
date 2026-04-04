class Solution(object):
    def solveSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: None Do not return anything, modify board in-place instead.
        """

        # Bitmasks for rows, cols, and boxes
        rows = [0] * 9
        cols = [0] * 9
        boxes = [0] * 9

        empty = []

        # Initialize masks
        for i in range(9):
            for j in range(9):
                if board[i][j] == '.':
                    empty.append((i, j))
                else:
                    num = int(board[i][j]) - 1
                    mask = 1 << num
                    rows[i] |= mask
                    cols[j] |= mask
                    boxes[(i // 3) * 3 + j // 3] |= mask

        # Backtracking with MRV heuristic
        def backtrack():
            if not empty:
                return True

            # Choose cell with minimum options (MRV)
            min_options = 10
            min_index = -1

            for idx in range(len(empty)):
                r, c = empty[idx]
                used = rows[r] | cols[c] | boxes[(r // 3) * 3 + c // 3]
                options = 9 - bin(used).count('1')

                if options < min_options:
                    min_options = options
                    min_index = idx

            # Swap to process best candidate first
            empty[0], empty[min_index] = empty[min_index], empty[0]
            r, c = empty.pop(0)

            b = (r // 3) * 3 + c // 3
            used = rows[r] | cols[c] | boxes[b]

            for num in range(9):
                mask = 1 << num
                if not (used & mask):
                    # Place number
                    board[r][c] = str(num + 1)
                    rows[r] |= mask
                    cols[c] |= mask
                    boxes[b] |= mask

                    if backtrack():
                        return True

                    # Undo
                    board[r][c] = '.'
                    rows[r] ^= mask
                    cols[c] ^= mask
                    boxes[b] ^= mask

            empty.insert(0, (r, c))
            return False

        backtrack()
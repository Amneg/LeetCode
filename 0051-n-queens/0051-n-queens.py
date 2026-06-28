class Solution:
    def solveNQueens(self, n):
        res = []
        board = [['.'] * n for _ in range(n)]

        cols = [False] * n
        diag1 = [False] * (2 * n - 1)
        diag2 = [False] * (2 * n - 1)

        def dfs(r):
            if r == n:
                res.append([''.join(row) for row in board])
                return

            for c in range(n):
                d1 = r - c + n - 1
                d2 = r + c

                if cols[c] or diag1[d1] or diag2[d2]:
                    continue

                cols[c] = diag1[d1] = diag2[d2] = True
                board[r][c] = 'Q'

                dfs(r + 1)

                board[r][c] = '.'
                cols[c] = diag1[d1] = diag2[d2] = False

        dfs(0)
        return res
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # [ [], [], [], [], [], [], [], [], [] ]
        rowset = [set() for __ in range(9)]
        colset = [set() for __ in range(9)]
        boxset = [set() for __ in range(9)]

        for row in range(9):
            for col in range(9):
                val = board[row][col]

                if val == '.':
                    continue

                if val in rowset[row]:
                    return False
                rowset[row].add(val)

                if val in colset[col]:
                    return False
                colset[col].add(val)

                box = (row // 3) * 3 + (col // 3)
                if val in boxset[box]:
                    return False
                boxset[box].add(val)
        return True       
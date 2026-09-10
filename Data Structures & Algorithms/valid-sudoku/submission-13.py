class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rowset = [set() for _ in range(9)]
        colset = [set() for _ in range(9)]
        boxset = [set() for _ in range(9)]

        for r in range(9):
            for c in range(9):
                val = board[r][c]
                if val == ".":
                    continue
                
                if val in rowset[r]:
                    return False
                rowset[r].add(val)

                if val in colset[c]:
                    return False
                colset[c].add(val)

                boxes = (r // 3) + (c // 3) * 3
                if val in boxset[boxes]:
                    return False
                boxset[boxes].add(val)
        return True

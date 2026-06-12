class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rowS = [set() for _ in range(9)]
        colS = [set() for _ in range(9)]
        boxS = [set() for _ in range(9)]

        for r in range(9):
            for c in range(9):
                val = board[r][c]

                if val == '.':
                    continue
                
                if val in rowS[r]:
                    return False
                rowS[r].add(val)

                if val in colS[c]:
                    return False
                colS[c].add(val)

                boxIdx = (r // 3) * 3 + (c // 3)
                if val in boxS[boxIdx]:
                    return False
                boxS[boxIdx].add(val)
        return True
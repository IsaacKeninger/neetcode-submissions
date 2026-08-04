class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        cset = [set() for __ in range(9)]
        rset = [set() for __ in range(9)]
        bset = [set() for __ in range(9)]

        for row in range(9):
            for col in range(9):
                val = board[row][col]
                if val == '.':
                    continue
                if val in rset[row]:
                    return False
                rset[row].add(val)
                if val in cset[col]:
                    return False
                cset[col].add(val)
                bidx = (col // 3) * 3 + (row // 3)
                if val in bset[bidx]:
                    return False
                bset[bidx].add(val)
        return True
                
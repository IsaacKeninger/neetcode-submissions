class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rowset = defaultdict(set)
        colset = defaultdict(set)
        boxset = defaultdict(set)
        for i in range(len(board)):
            for j in range(len(board)):
                val = board[i][j]

                if val == '.':
                    continue

                if val in rowset[i]:
                    return False
                rowset[i].add(val)

                if val in colset[j]:
                    return False
                colset[j].add(val)

                box_idx = (i // 3) * 3 + (j // 3)
                if val in boxset[box_idx]:
                    return False
                boxset[box_idx].add(val)

        return True
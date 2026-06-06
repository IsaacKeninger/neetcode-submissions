class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rowSet = [set() for _ in range(9)]
        colSet = [set() for _ in range(9)]
        boxes = [set() for _ in range(9)]

        for r in range(9):
            for c in range(9):

                if board[r][c] == ".":
                    continue

                if board[r][c] in rowSet[r]:
                    return False
                rowSet[r].add(board[r][c])
                if board[r][c] in colSet[c]:
                    return False
                colSet[c].add(board[r][c])  

                boxidx = (r // 3) * 3 + (c // 3)
                if board[r][c] in boxes[boxidx]:
                    return False
                boxes[boxidx].add(board[r][c])
        return True           
                

        
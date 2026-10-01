class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = [set() for _ in range(9)]
        cols = [set() for _ in range(9)]
        boxes = [set() for _ in range(9)]

            #to go in sudoku

        for r in range(9):
            for c in range(9):
                value = board[r][c]
                if value == ".":
                    continue

                #duplicate row checker
        
                if value in rows[r]:
                    return False
                else:
                    rows[r].add(value)
        
                #duplicate cols checker

                if value in cols[c]:
                    return False
                else:
                    cols[c].add(value)
        
                #boxes calculation
                box_index = (r // 3) * 3 + (c // 3)

                #box checker
                if value in boxes[box_index]:
                    return False
                else:
                    boxes[box_index].add(value)
        
        return True
            
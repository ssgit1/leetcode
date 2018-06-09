class Solution:
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        validChars = []
        col = []
        row = []
        box = []
        for i in range(0,9):
            validChars.append(str(i+1))
            col.append(set())
            row.append(set())
            box.append(set())          
        for i in range(0,9):
            for j in range(0,9):
                rc = board[i][j]
                if rc == ".":
                    continue
                if rc not in validChars:
                    return False
                boxIdx = 3*(i//3) + (j//3) 
                if rc in row[i] or rc in col[j] or rc in box[boxIdx]:
                    return False
                row[i].add(rc)
                col[j].add(rc)
                box[boxIdx].add(rc)        
        return True        

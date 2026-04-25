class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # travel through an matrix
        for row in range(9):
            seen = set()
            for i in range(9):
                element = board[row][i]
                # dùng set thì 
                if "1" <= element <= "9":
                    if element in seen:
                        return False
                    seen.add(element)
        for col in range(9):
            seen = set()
            for i in range(9):
                element = board[i][col]
                if "1" <= element <= "9":
                    if element in seen:
                        return False
                    seen.add(element)
        
        x_list = [1,1,1,-1,-1,-1,0,0]
        y_list = [1,0,-1,-1,0,1,1,-1]
        for row in range(1,8,3):
            for col in range(1,8,3):
                seen = set()
                for i in range(8):
                    x = x_list[i] + row
                    y = y_list[i] + col
                    element = board[x][y]
                    if "1" <= element <= "9":
                        if element in seen:
                            return False
                        seen.add(element) 
        return True




class Solution:
    def numRookCaptures(self, board: list[list[str]]) -> int:
    
        def findRook(board):
            for i in range(len(board)) :
                for j in range(len(board[0])) :
                    if board[i][j] == "R" :
                        return i , j

        x , y = findRook(board)
        
        count = 0

        i = x - 1
        while i >= 0 and board[i][y] == ".":i -= 1
        count += 1 if i >= 0 and board[i][y] == "p" else 0

        i = x + 1
        while i < len(board) and board[i][y] == ".": i += 1
        count += 1 if i < len(board) and board[i][y] == "p" else 0

        i = y - 1
        while i >= 0 and board[x][i] == ".":i -= 1
        count += 1 if i >= 0 and board[x][i] == "p" else 0

        i = y + 1
        while i < len(board[0]) and board[x][i] == ".": i += 1
        count += 1 if i < len(board[0]) and board[x][i] == "p" else 0

        return count
class NQueensSolver:
    def __init__(self, n):
        self.n = n
        self.board = [-1]*n
        self.columns = [False]*n
        self.majorDiagonals = [False]*(2*n - 1)
        self.minorDiagonals = [False]*(2*n - 1)
        self.solutions = []

    def insertQueens(self, row):
        if row == self.n:
            self.solutions.append(self.board[:])
            return

        for col in range(self.n):
            majorIndex = row - col + (self.n - 1)
            minorIndex = row + col
            
            if not self.columns[col] and not self.majorDiagonals[majorIndex] and not self.minorDiagonals[minorIndex]:
                self.board[row] = col
                self.columns[col] = True
                self.majorDiagonals[majorIndex] = True
                self.minorDiagonals[minorIndex] = True
                
                self.insertQueens(row + 1)
                
                self.board[row] = -1
                self.columns[col] = False
                self.majorDiagonals[majorIndex] = False
                self.minorDiagonals[minorIndex] = False

    def buildBoard(self, board):
        solutionBoard = []
        for i in range(self.n):
            rowList = ['x'] * self.n
            qCol = board[i]
            rowList[qCol] = 'Q'
            solutionBoard.append("".join(rowList))
        
        totalQueens = sum(row.count('Q') for row in solutionBoard)
        return solutionBoard, totalQueens
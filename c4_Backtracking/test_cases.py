import unittest
from problem_1 import NQueensSolver

class TestNqueensProblem(unittest.TestCase):
    #Case description: A board is defined as 4x4 in size. On this board it is possible to position 4 queens in 2 different ways following the imposed rules (avoiding conflict in the same row, column and diagonals);
    def test_case_1(self):
        n = 4
        solver = NQueensSolver(n)
        solver.insertQueens(0)
        resultSolutions = len(solver.solutions)
        expectedSolutions = 2
        expectedAmountQueens = 4

        for solution in solver.solutions:
            board, totalQueens = solver.buildBoard(solution)
            
        resultQueens=totalQueens
        
        if not(expectedSolutions == resultSolutions and expectedAmountQueens == resultQueens):
            print("Test failed!")
        else:
            print("Test pass!")
    
    #Case description: A board is defined as 1x1 in size. On this board there is only one possible solution to position n queens on the board (in this case n queens is equal to 1);
    def test_case_2(self):
        n = 1
        solver = NQueensSolver(n)
        solver.insertQueens(0)
        resultSolutions = len(solver.solutions)
        expectedSolutions = 1
        expectedAmountQueens = 1

        for solution in solver.solutions:
            board, totalQueens = solver.buildBoard(solution)
            
        resultQueens=totalQueens
        
        if not(expectedSolutions == resultSolutions and expectedAmountQueens == resultQueens):
            print("Test failed!")
        else:
            print("Test pass!")
    
    #Case description: A board is defined as 6x6 in size. On this board it is possible to position n queens in 4 different ways following the imposed rules (avoiding conflict in the same row, column and diagonals);
    def test_case_3(self):
        n = 6
        solver = NQueensSolver(n)
        solver.insertQueens(0)
        resultSolutions = len(solver.solutions)
        expectedSolutions = 4
        expectedAmountQueens = 6

        for solution in solver.solutions:
            board, totalQueens = solver.buildBoard(solution)
            
        resultQueens=totalQueens
        
        if not(expectedSolutions == resultSolutions and expectedAmountQueens == resultQueens):
            print("Test failed!")
        else:
            print("Test pass!")
    
    
if __name__ == '__main__':
    unittest.main()

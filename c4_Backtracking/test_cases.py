import unittest
from problem_1 import NQueensSolver

class TestNqueensProblem(unittest.TestCase):
    def test_case_1(self):
        n = 4
        solver = NQueensSolver(n)
        solver.insertQueens(0)
                
        result = len(solver.solutions)
        expected_solutions = 2
        
        if expected_solutions == result:
            print("Test pass!")
        else:
            print("Test failed!")
    
    def test_case_2(self):
        n = 1
        solver = NQueensSolver(n)
        solver.insertQueens(0)
        
        result = len(solver.solutions)
        expected_solutions = 1
        
        if expected_solutions == result:
            print("Test pass!")
        else:
            print("Test failed!")
    
    def test_case_3(self):
        n = 6
        solver = NQueensSolver(n)
        solver.insertQueens(0)
        
        result = len(solver.solutions)
        expected_solutions = 4
        
        if expected_solutions == result:
            print("Test pass!")
        else:
            print("Test failed!")
    
if __name__ == '__main__':
    unittest.main()

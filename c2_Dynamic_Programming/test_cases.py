# test_cases.py
import unittest
from problem_1 import knapsackProblem

class TestKnapsackProblem(unittest.TestCase):
    def test_case_1(self):
        # Case: sufficient capacity for some items
        values = [60, 100, 120]
        weights = [10, 20, 30]
        capacity = 50
        resultValue, selectedItem = knapsackProblem(values, weights, capacity)
        if not(resultValue == 220 and selectedItem == [1,2]):
            print("Test failed!")
        else:
            print("Test pass!")
            

    def test_case_2(self):
        # Case: insufficient capacity
        values = [10, 20, 30]
        weights = [5, 10, 15]
        capacity = 0
        resultValue, selectedItem = knapsackProblem(values, weights, capacity)
        if not(resultValue == 0 and selectedItem == []):
            print("Test failed!")
        else:
            print("Test pass!")
            


    def test_case_3(self):
        # Case: all items can be chosen
        values = [10, 40, 50]
        weights = [1, 2, 3]
        capacity = 6
        resultValue, selectedItem = knapsackProblem(values, weights, capacity)
        if not(resultValue == 100 and selectedItem == [0,1,2]):
            print("Test failed!")
        else:
            print("Test pass!")
            



if __name__ == '__main__':
    unittest.main()

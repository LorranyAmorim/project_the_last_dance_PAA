import unittest
from problem_1 import Item, BranchAndBound

class TestKnapsackProblemBandB(unittest.TestCase):
    """
    Case description: Sufficient capacity for some items.
    It is expected to select items with indexes [1, 2], totaling 220.
    """
    def test_case_1(self):
        values = [60, 100, 120]
        weights = [10, 20, 30]
        capacity = 50
        items = [Item(value=val, weight=wt) for val, wt in zip(values, weights)]
        bnb = BranchAndBound(items, capacity)
        resultValue, selectedItem = bnb.KnapsackBandB()
        expectedValue = 220
        expectedSelected = [1, 2]
        if not(resultValue == expectedValue and selectedItem==expectedSelected):
            print("Test failed!")
        else:
            print("Test pass!")



    """
    Case description: insufficient capacity.
    It is expected that no items will be selected, totaling 0.
    """
    def test_case_2(self):
        values = [10, 20, 30]
        weights = [5, 10, 15]
        capacity = 0
        items = [Item(value=val, weight=wt) for val, wt in zip(values, weights)]
        bnb = BranchAndBound(items, capacity)
        resultValue, selectedItem = bnb.KnapsackBandB()
        expectedValue = 0
        expectedSelected = []
        if not(resultValue == expectedValue and selectedItem==expectedSelected):
            print("Test failed!")
        else:
            print("Test pass!")



        """
       Case description: All items can be selected.
       It is expected to select all items, totaling value 100.
        """
    def test_case_3(self):
        values = [10, 40, 50]
        weights = [1, 2, 3]
        capacity = 6
        items = [Item(value=val, weight=wt) for val, wt in zip(values, weights)]
        bnb = BranchAndBound(items, capacity)
        resultValue, selectedItem = bnb.KnapsackBandB()
        expectedValue = 100
        expectedSelected = [0, 1, 2]
        if not(resultValue == expectedValue and selectedItem==expectedSelected):
            print("Test failed!")
        else:
            print("Test pass!")




if __name__ == '__main__':
    unittest.main()

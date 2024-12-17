import unittest
from problem_3 import Node, findMaxPreOrder, findMinInOrder, findAveragePosOrder

class TestArvore(unittest.TestCase):
    """
    Case description: maximum value is in the leaf node on the right;
    The minimum value is in a node on the left;
    The average is calculated considering all nodes.
    """
    def test_case_1(self):
        root = Node(10)
        root.left = Node(5)
        root.right = Node(20)
        root.left.left = Node(3)
        root.left.right = Node(7)
        root.right.left = Node(15)
        root.right.right = Node(25)
        resultMax = findMaxPreOrder(root)
        resultMin = findMinInOrder(root)
        resultAverage = findAveragePosOrder(root)
        if not(resultMax==25 and resultMin==3 and str(resultAverage).startswith("12.14")):
            print("Test failed!")
        else:
            print("Test pass!")
            
    """
    Case description: maximum value is in the leaf node on the right; 
    The minimum value is in a leaf node on the left;
    The average is calculated considering all nodes.
    """
    def test_case_2(self):
        root = Node(50)
        root.left = Node(45)
        root.right = Node(60)
        root.left.left = Node(40)
        root.right.right = Node(70)
        resultMax = findMaxPreOrder(root)
        resultMin = findMinInOrder(root)
        resultAverage = findAveragePosOrder(root)
        if not(resultMax==70 and resultMin==40 and str(resultAverage).startswith("53")):
            print("Test failed!")
        else:
            print("Test pass!")
            
    """    
    Case description: maximum value is the leaf node;
    The minimum value is the root node;
    The average is calculated considering negative values. 
    """
    def test_case_3(self):
        root = Node(-10)
        root.right = Node(-5)
        resultMax = findMaxPreOrder(root)
        resultMin = findMinInOrder(root)
        resultAverage = findAveragePosOrder(root)
        if not(resultMax==-5 and resultMin==-10 and str(resultAverage).startswith("-7.5")):
            print("Test failed!")
        else:
            print("Test pass!")



if __name__=='__main__':
    unittest.main()

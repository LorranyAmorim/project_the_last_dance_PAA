# test_cases.py
import unittest
from problem_2 import Kruskall

class TestKruskallProblem(unittest.TestCase):
    def test_case_1(self):
       k = Kruskall(3)
       k.createVertexList(0, "A")
       k.createVertexList(1, "B")
       k.createVertexList(2, "C")

       k.createEdgeList(1, 0, 1)  
       k.createEdgeList(2, 1, 2)  
       k.createEdgeList(3, 0, 2)  
       
       result = k.kruskalProblem()

       expected = [("A", "B", 1), ("B", "C", 2)]

       check=self.assertCountEqual(result,expected)

       if check!=AssertionError:
           print("Test pass!")
       else:
           print("Test failed!")

    def test_case_2(self):
        k = Kruskall(4)
        k.createVertexList(0, "A")
        k.createVertexList(1, "B")
        k.createVertexList(2, "C")
        k.createVertexList(3, "D")

        k.createEdgeList(1, 0, 1)  # A-B
        k.createEdgeList(2, 2, 3)  # C-D

        result = k.kruskalProblem()

        expected = [("A", "B", 1), ("C", "D", 2)]

        check=self.assertCountEqual(result, expected)
        if check!=AssertionError:
            print("Test pass!")
        else:
            print("Test failed!")
        

    def test_case_3(self):
        k = Kruskall(3)
        k.createVertexList(0, "A")
        k.createVertexList(1, "B")
        k.createVertexList(2, "C")
        
        k.createEdgeList(1, 0, 1)
        k.createEdgeList(2, 0, 1)
        k.createEdgeList(3, 1, 2)  
        result = k.kruskalProblem()
        
        expected = [("A", "B", 1), ("B", "C", 3)]
        
        self.assertCountEqual(result, expected)

        check=self.assertCountEqual(result, expected)

        if check!=AssertionError:
            print("Test pass!")
        else:
            print("Test failed!")
            

if __name__ == '__main__':
    unittest.main()

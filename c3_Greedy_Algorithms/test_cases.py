import unittest
from problem_2 import Kruskall

class TestKruskallProblem(unittest.TestCase):
    #Case description: sorts the edges by weight;
    #Builds the minimum spanning tree without cycles;
    #Selects the lowest weight edges to connect the vertices.
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


    #Case description: handles disconnected components;
    #Sorts the edges by weight;
    #Builds the minimum spanning trees independently for each connected component;
    #Selects the lowest weight edges for each component without forming cycles.
    def test_case_2(self):
        k = Kruskall(4)
        k.createVertexList(0, "A")
        k.createVertexList(1, "B")
        k.createVertexList(2, "C")
        k.createVertexList(3, "D")
        k.createEdgeList(1, 0, 1)  
        k.createEdgeList(2, 2, 3)  
        result = k.kruskalProblem()
        expected = [("A", "B", 1), ("C", "D", 2)]
        check=self.assertCountEqual(result, expected)
        if check!=AssertionError:
            print("Test pass!")
        else:
            print("Test failed!")
        
        
 
    #Case description: processes graphs with multiple edges between the same pair of vertices;
    #Sorts the edges by weight;
    #Ensures no duplicate edges are selected;
    #Builds the minimum spanning tree without cycles;
    #Selects the lowest weight edges to connect all vertices.
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

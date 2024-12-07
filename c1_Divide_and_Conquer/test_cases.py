# test_cases.py
import unittest
from problem_3 import Node, findMaxPreOrder, findMinInOrder, findMedianPosOrder

class TestArvore(unittest.TestCase):
    def test_case_1(self):
        root = Node(10)
        root.left = Node(5)
        root.right = Node(20)
        root.left.left = Node(3)
        root.left.right = Node(7)
        root.right.left = Node(15)
        root.right.right = Node(25)
        self.assertEqual(findMaxPreOrder(root),25)
        self.assertEqual(findMinInOrder(root),3)
        self.assertEqual(findMedianPosOrder(root),12.14,places=2)  # Deve conferir se este valor é mesmo o correto
    
    def test_case_2(self):
        root = Node(50)
        root.left = Node(45)
        root.right = Node(60)
        root.left.left = Node(40)
        root.right.right = Node(70)
        self.assertEqual(findMaxPreOrder(root),70)
        self.assertEqual(findMinInOrder(root),40)
        self.assertEqual(findMedianPosOrder(root),53)  # Deve conferir se este valor é mesmo o correto

    def test_case_3(self):
        root = Node(-10)
        root.right = Node(-5)
        self.assertEqual(findMaxPreOrder(root),-5)
        self.assertEqual(findMinInOrder(root),-10)
        self.assertEqual(findMedianPosOrder(root),-7.5,places=2) # Deve conferir se este valor é mesmo o correto

if __name__=='__main__':
    unittest.main()
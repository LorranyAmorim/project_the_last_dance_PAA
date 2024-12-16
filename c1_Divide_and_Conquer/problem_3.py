class Node:
    def __init__(self, value):         
        self.value = value             
        self.left = None               
        self.right = None               

def findMaxPreOrder(node):
    if node is None:                   
        return float('-inf')           
    currentValue = node.value             
    leftMax = findMaxPreOrder(node.left)  
    rightMax = findMaxPreOrder(node.right)
    return max(currentValue,leftMax,rightMax)   

def findMinInOrder(node):
    if node is None:
        return float('inf')
    leftMin = findMinInOrder(node.left)
    currentValue = node.value
    rightMin = findMinInOrder(node.right)
    return min(leftMin,currentValue,rightMin)     

def postOrderValues(node):
    if node is None:
        return []
    return postOrderValues(node.left) + postOrderValues(node.right) + [node.value]

def findAveragePosOrder(node):
    values = postOrderValues(node)
    n = len(values)
    if n == 0:
        return float('inf')
    return sum(values) / n
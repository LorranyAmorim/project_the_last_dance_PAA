#Usando cada caminhamento para encontrar o maior, menor e a media do valor da árvore binária
class Node:
    def __init__(self, value):         
        self.value = value             
        self.left = None               
        self.right = None               

#pre-order
def findMaxPreOrder(node):
    if node is None:                   
        return float('-inf')           
    currentValue = node.value             
    leftMax = findMaxPreOrder(node.left)  
    rightMax = findMaxPreOrder(node.right)
    return max(currentValue,leftMax,rightMax)   

#in-order
def findMinInOrder(node):
    if node is None:
        return float('inf')
    leftMin = findMinInOrder(node.left)
    currentValue = node.value
    rightMin = findMinInOrder(node.right)
    return min(leftMin,currentValue,rightMin)     

#pos-order
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
class Item:
    def __init__(self, value, weight):
        self.value = value
        self.weight = weight

class Node:
    def __init__(self, index, accumulatedValue, accumulatedWeight, setSelected=None):
        self.index = index 
        self.accumulatedValue = accumulatedValue
        self.accumulatedWeight = accumulatedWeight
        self.setSelected = setSelected if setSelected is not None else []
        self.upperLimit = 0

class PriorityQueue:
    def __init__(self):
        self.data = []

    def insert(self, node):
        import heapq
        heapq.heappush(self.data, (-node.upperLimit, node))

    def remover(self):
        import heapq
        if not self.data:
            return None
        return heapq.heappop(self.data)[1]  
    
    def isEmpty(self):
        return len(self.data) == 0

class BranchAndBound:
    def __init__(self, items, W):
        self.items = items
        self.W = W

    def calcUpperLimit(self, node):
        value = node.accumulatedValue
        remainWeight = self.W - node.accumulatedWeight
        i = node.index
        n = len(self.items)

        while i < n and remainWeight > 0:
            if self.items[i].weight <= remainWeight:
                value += self.items[i].value
                remainWeight -= self.items[i].weight
            else:
                fraction = remainWeight / self.items[i].weight
                value += self.items[i].value * fraction
                remainWeight = 0
            i += 1

        return value

    def KnapsackBandB(self):
        bestValue = 0
        bestSet = []

        rootNode = Node(index=0, accumulatedValue=0, accumulatedWeight=0, setSelected=[])

        rootNode.upperLimit = self.calcUpperLimit(rootNode)

        PQ = PriorityQueue()
        PQ.insert(rootNode)

        while not PQ.isEmpty():
            currentNode = PQ.remover()

            if currentNode.upperLimit <= bestValue:
                continue

            if currentNode.index == len(self.items):
                if currentNode.accumulatedValue > bestValue:
                    bestValue = currentNode.accumulatedValue
                    bestSet = currentNode.setSelected
                continue

            nextItem = self.items[currentNode.index]

            if currentNode.accumulatedWeight + nextItem.weight <= self.W:
                includeNode = Node(
                    index=currentNode.index + 1,
                    accumulatedValue=currentNode.accumulatedValue + nextItem.value,
                    accumulatedWeight=currentNode.accumulatedWeight + nextItem.weight,
                    setSelected=currentNode.setSelected + [currentNode.index]  
                )
                includeNode.upperLimit = self.calcUpperLimit(includeNode)

                if includeNode.upperLimit > bestValue:
                    PQ.insert(includeNode)

            excludeNode = Node(
                index=currentNode.index + 1,
                accumulatedValue=currentNode.accumulatedValue,
                accumulatedWeight=currentNode.accumulatedWeight,
                setSelected=currentNode.setSelected
            )
            excludeNode.upperLimit = self.calcUpperLimit(excludeNode)

            if excludeNode.upperLimit > bestValue:
                PQ.insert(excludeNode)

        return (bestValue, bestSet)
    

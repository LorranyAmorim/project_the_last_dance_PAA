def knapsackProblem(itemValues,itemWeights,maxCapacity):
    n = len(itemValues)     
    dpTable = [[0 for _ in range(maxCapacity+1)] for _ in range(n+1)] 
    
    for i in range(1, n+1):  
        for capacity in range(1, maxCapacity+1): 
            dpTable[i][capacity] = dpTable[i-1][capacity] 

            if itemWeights[i-1] <= capacity: 
                items = itemValues[i-1] + dpTable[i-1][capacity - itemWeights[i-1]] 
                if items > dpTable[i][capacity]:
                    dpTable[i][capacity] = items
    
    maxValue = dpTable[n][maxCapacity]
    selectedItems = []
    capacity = maxCapacity

    for i in range(n, 0, -1):
        if dpTable[i][capacity] != dpTable[i-1][capacity]:
            selectedItems.append(i-1)
            capacity = capacity - itemWeights[i-1]
    
    selectedItems.reverse()
    return maxValue, selectedItems
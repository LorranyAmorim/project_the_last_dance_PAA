def knapsackProblem(itemValue,itemWeight,maxCapacityBag):
    n = len(itemValue)     
    matrizValuesAndItens = [[0 for _ in range(maxCapacityBag+1)] for _ in range(n+1)] 
    
    for i in range(1, n+1):  
        for c in range(1, maxCapacityBag+1): 
            matrizValuesAndItens[i][c] = matrizValuesAndItens[i-1][c] 

            if itemWeight[i-1] <= c: 
                items = itemValue[i-1] + matrizValuesAndItens[i-1][c - itemWeight[i-1]] 
                if items > matrizValuesAndItens[i][c]:
                    matrizValuesAndItens[i][c] = items
    
    maxValue = matrizValuesAndItens[n][maxCapacityBag]
    selectedItems = []
    c = maxCapacityBag

    for i in range(n, 0, -1):
        if matrizValuesAndItens[i][c] != matrizValuesAndItens[i-1][c]:
            selectedItems.append(i-1)
            c = c - itemWeight[i-1]
    
    selectedItems.reverse()
    return maxValue, selectedItems
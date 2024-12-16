def knapsackProblem(v,w,W):
    #v = lista dos valores de cada item
    #w = lista dos pesos de cada item
    #W = capacidade maxima da mochila
    #n = quantidade de itens
    #K = valor máximo de itens e seus pesos na mochila considerando a capacidade

    n=len(v)
    K=[[0 for _ in range(W+1)] for _ in range(n+1)]
    
    for i in range(1,n+1):
        for cap in range(1,W+1):
            K[i][cap]=K[i-1][cap]

            if w[i-1]<=cap:
                itemValue=v[i-1]+K[i-1][cap-w[i-1]]
                if itemValue>K[i][cap]:
                    K[i][cap]=itemValue
    
    maxValue=K[n][W]
    selectedItems=[]
    cap = W

    for i in range(n,0,-1):
        if K[i][cap]!=K[i-1][cap]:
            selectedItems.append(i-1)
            cap=cap-w[i-1]
    
    selectedItems.reverse()
    return maxValue, selectedItems
class Kruskall:
    def __init__(self,size):
        self.size = size
        self.edges = []
        self.vertex = ['']*size
    
    def createEdgeList(self,weight,u,v):
        if 0 <= u < self.size and 0 <= v < self.size:
            self.edges.append((u,v,weight))
    
    def createVertexList(self,vertex,d):
        if 0 <= vertex < self.size:
            self.vertex[vertex] = d
    
    def find(self,parent,i):
        if parent[i]==i:
            return i
        return self.find(parent,parent[i])
    
    def union(self,parent,rank,x,y):
        xRoot = self.find(parent,x)
        yRoot = self.find(parent,y)
        if rank[xRoot] < rank[yRoot]:
            parent[xRoot]=yRoot
        elif rank[xRoot]>rank[yRoot]:
            parent[yRoot]= xRoot
        else:
            parent[yRoot]=xRoot
            rank[xRoot]+=1
    
    def kruskalProblem(self):
        
        self.edges=sorted(self.edges, key=lambda item: item[2])
        parent = [i for i in range(self.size)]
        rank = [0]*self.size

        result = []

        for u,v,weight in self.edges:
            x = self.find(parent,u)
            y = self.find(parent,v)

            if x != y:
                result.append((u,v,weight))
                self.union(parent,rank,x,y)

        mstResult=[]

        for(u,v,weight) in result:
            mstResult.append((self.vertex[u],self.vertex[v],weight))

        return mstResult

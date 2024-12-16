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

if __name__ == '__main__':
    g = Kruskall(7)
    g.createVertexList(0, 'A')
    g.createVertexList(1, 'B')
    g.createVertexList(2, 'C')
    g.createVertexList(3, 'D')
    g.createVertexList(4, 'E')
    g.createVertexList(5, 'F')
    g.createVertexList(6, 'G')
    
    g.createEdgeList(0, 1, 4)  #A-B,  4
    g.createEdgeList(0, 6, 10) #A-G, 10
    g.createEdgeList(0, 2, 9)  #A-C,  9
    g.createEdgeList(1, 2, 8)  #B-C,  8
    g.createEdgeList(2, 3, 5)  #C-D,  5
    g.createEdgeList(2, 4, 2)  #C-E,  2
    g.createEdgeList(2, 6, 7)  #C-G,  7
    g.createEdgeList(3, 4, 3)  #D-E,  3
    g.createEdgeList(3, 5, 7)  #D-F,  7
    g.createEdgeList(4, 6, 6)  #E-G,  6
    g.createEdgeList(5, 6, 11) #F-G, 11
    
    print("Kruskal's Algorithm MST:")
    print(g.kruskalProblem())

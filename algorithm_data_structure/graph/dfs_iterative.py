# -*- coding: utf-8 -*-

class Graph: 
    def __init__(self, V): 
        self.V = V 
        self.adj = [[] for i in range(V)] 

    def addEdge(self, v, w): 
        self.adj[v].append(w) # Add w to v’s list. 
    
    def DFSUtil(self, s, visited): 
        stack = [] 
        stack.append(s) 

        while (len(stack) != 0): 
            s = stack.pop() 
            if not visited[s]:
                print(s, end = " ")
                visited[s] = True

            for ele in self.adj[s]:
                if (not visited[ele]): 
                    stack.append(ele)

    def DFS(self): 
        visited = [False] * self.V 
        for i in range(self.V): 
            if (not visited[i]): 
                self.DFSUtil(i, visited) 

# Driver Code 
if __name__ == '__main__': 

    g = Graph(5) # Total 5 vertices in graph 
    g.addEdge(1, 0) 
    g.addEdge(2, 1) 
    g.addEdge(3, 4) 
    g.addEdge(4, 0) 

    print("Following is Depth First Traversal") 
    g.DFS() 

# This code is contributed by PranchalK 


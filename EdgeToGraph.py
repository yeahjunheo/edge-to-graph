from collections import deque

# The program just works around the BFS and DFS in making a graph when edges are given
class Graph:
    
    # Constructor
    def __init__(self, edges, numNodes):
        
        # This will create create a 
        self.adjList = [[] for _ in range(numNodes)]
        
        for (scr, dest) in edges:
            self.adjList[scr].append(dest)
            self.adjList[dest].append(scr)

    
if __name__ == "__main__":
    
    # An array of edges containing the initial point and the destination
    edges = [
        (1, 2), (1, 3), (1, 4), 
        (2, 5), (2, 6), 
        (4, 7), (4, 8),
        (5, 9), (5, 10),
        (7, 11), (7, 12)
    ]
    
    # Total number of nodes will be greater
    numNodes = 15
    
    currentGraph = Graph(edges, numNodes)
    
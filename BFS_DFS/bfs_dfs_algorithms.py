from pickle import NONE
from queue import Queue

adjacency_list = {"A": ["B", "C"],
          "B": ["A", "C", "D"],
          "C": ["A", "B", "D", "E"],
          "D": ["B", "C", "E", "F"],
          "E": ["C", "D"],
          "F": ["D"]
        }

class Graph:

    def __init__(self):
        self.visited = {}
        self.level = {}
        self.parent = {}
        self.queue = Queue()
        self.bfs_traversal_output = []


    def bfs(self, graph, start):

        for node in graph.keys():
            self.visited[node] = False
            self.level[node] = -1
            self.parent[node] = NONE
        
        self.visited[start] = True
        self.level[start] = 0
        self.queue.put(start)

        while not self.queue.empty():
            u = self.queue.get()
            self.bfs_traversal_output.append(u)

            for v in graph[u]:
                if not self.visited[v]:
                    self.visited[v] = True
                    self.parent[v] = u
                    self.level[v] = self.level[u] + 1
                    self.queue.put(v)

        return self.bfs_traversal_output
        

    def dfs(self, graph, start):
        stack = [] 
        stack.append(start)
        self.visited = set()  
        self.visited.add(start)

        while stack:
            vertex = stack.pop()
            nodes = graph[vertex]
            for w in nodes:
                if w not in self.visited:
                    stack.append(w)
                    self.visited.add(w)
            print(vertex)




if __name__ == "__main__":

    g = Graph()
    print("bfs traversal: " + str(g.bfs(adjacency_list, "A")))
    print(g.level)
    g.dfs(adjacency_list, "A")
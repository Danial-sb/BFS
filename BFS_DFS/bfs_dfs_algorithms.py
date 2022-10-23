from pickle import NONE
from queue import Queue

adjacency_list = {
  '5' : ['3','7'],
  '3' : ['2', '4'],
  '7' : ['8'],
  '2' : [],
  '4' : ['8'],
  '8' : []
}

class Graph:

    def __init__(self):
        self.visited = {}
        self.level = {}
        self.parent = {}
        self.queue = Queue()
        self.bfs_traversal_output = []


    def bfs(self):

        for node in adjacency_list.keys():
            self.visited[node] = False
            self.level[node] = -1
            self.parent[node] = NONE
        
        root = '5'
        self.visited[root] = True
        self.level[root] = 0
        self.queue.put(root)

        while not self.queue.empty():
            u = self.queue.get()
            self.bfs_traversal_output.append(u)

            for v in adjacency_list[u]:
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
            return vertex




if __name__ == "__main__":

    g = Graph()
    print(g.bfs())
    print(g.level)
    print(g.dfs(adjacency_list, '5'))
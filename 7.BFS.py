from collections import deque

class Graph:
    def __init__(self):
        self.graph = {}

    def add_edge(self, u, v):
        if u not in self.graph:
            self.graph[u] = []
        self.graph[u].append(v)

    def bfs(self, start):
        visited = set()
        queue = deque([start])

        while queue:
            current_node = queue.popleft()
            if current_node not in visited:
                print(current_node, end=' ')
                visited.add(current_node)
                if current_node in self.graph:
                    queue.extend(self.graph[current_node])

# Example usage:
if __name__ == "__main__":
    # Create a sample graph
    g = Graph()
    g.add_edge(1, 2)
    g.add_edge(1, 3)
    g.add_edge(2, 4)
    g.add_edge(2, 5)
    g.add_edge(3, 6)
    g.add_edge(3, 7)

    # Perform BFS starting from node 1
    print("BFS starting from node 1:")
    g.bfs(1)

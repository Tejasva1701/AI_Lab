import numpy as np
import pandas as pd

class Graph:
    def __init__(self, num_vertices):
        self.num_vertices = num_vertices
        self.adj_matrix = np.zeros((num_vertices, num_vertices), dtype=int)

    def add_edge(self, u, v):
        self.adj_matrix[u][v] = 1
        self.adj_matrix[v][u] = 1

    def breadth_first_search(self, start_vertex):
        visited = np.zeros(self.num_vertices, dtype=bool)
        queue = [start_vertex]

        while queue:
            vertex = queue.pop(0)
            if not visited[vertex]:
                print(f"{vertex}")
                visited[vertex] = True
                neighbors = np.where(self.adj_matrix[vertex] == 1)[0]
                for neighbor in neighbors:
                    if not visited[neighbor]:
                        queue.append(neighbor)

if __name__ == "__main__":
    num_vertices = 6
    graph = Graph(num_vertices)

    # Add edges to the graph
    graph.add_edge(0, 1)
    graph.add_edge(0, 2)
    graph.add_edge(1, 3)
    graph.add_edge(1, 4)
    graph.add_edge(2, 4)
    graph.add_edge(3, 5)

    start_vertex = 0
    print("Breadth First Search:")
    graph.breadth_first_search(start_vertex)

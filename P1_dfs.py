import numpy as np
import pandas as pd

class Graph:
    def __init__(self, num_vertices):
        self.num_vertices = num_vertices
        self.adj_matrix = np.zeros((num_vertices, num_vertices), dtype=int)
        self.visited = np.zeros(num_vertices, dtype=bool)

    def add_edge(self, u, v):
        self.adj_matrix[u][v] = 1
        self.adj_matrix[v][u] = 1

    def depth_first_search(self, start_vertex):
        stack = [start_vertex]

        while stack:
            vertex = stack.pop()
            if not self.visited[vertex]:
                print(f"{vertex}")
                self.visited[vertex] = True
                neighbors = np.where(self.adj_matrix[vertex] == 1)[0]
                stack.extend(neighbors)

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
    print("Depth First Search:")
    graph.depth_first_search(start_vertex)

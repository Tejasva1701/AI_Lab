import numpy as np
import pandas as pd

class Node:
    def __init__(self, x, y, g_cost=0, h_cost=0):
        self.x = x
        self.y = y
        self.g_cost = g_cost  # Cost from the start node to this node
        self.h_cost = h_cost  # Heuristic cost to the goal node
        self.parent = None

    def f_cost(self):
        return self.g_cost + self.h_cost

def heuristic(node, goal):
    return abs(node.x - goal.x) + abs(node.y - goal.y)

def aostar(grid, start, goal):
    rows, cols = grid.shape
    open_set = []
    closed_set = set()

    start_node = Node(*start)
    goal_node = Node(*goal)

    open_set.append(start_node)

    while open_set:
        open_set.sort(key=lambda node: node.f_cost())
        current_node = open_set.pop(0)

        if current_node.x == goal_node.x and current_node.y == goal_node.y:
            path = []
            while current_node:
                path.append((current_node.x, current_node.y))
                current_node = current_node.parent
            path.reverse()
            return path

        closed_set.add((current_node.x, current_node.y))

        for dx, dy in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
            new_x, new_y = current_node.x + dx, current_node.y + dy
            if 0 <= new_x < rows and 0 <= new_y < cols and grid[new_x][new_y] != 1:
                if (new_x, new_y) not in closed_set:
                    neighbor = Node(new_x, new_y)
                    neighbor.g_cost = current_node.g_cost + 1
                    neighbor.h_cost = heuristic(neighbor, goal_node)
                    neighbor.parent = current_node

                    if neighbor in open_set:
                        open_set.remove(neighbor)

                    open_set.append(neighbor)

    return None

if __name__ == "__main__":
    grid = np.array([
        [0, 0, 0, 0, 1, 0],
        [0, 1, 1, 0, 1, 0],
        [0, 0, 0, 0, 0, 0],
        [1, 1, 1, 1, 1, 0],
        [0, 0, 0, 0, 0, 0]
    ])

    start = (0, 0)
    goal = (4, 5)

    path = aostar(grid, start, goal)

    if path:
        print("AO* Path:")
        df = pd.DataFrame(grid)
        for x, y in path:
            df.at[x, y] = 'P'
        print(df)
    else:
        print("No path found.")

import numpy as np
import pandas as pd

def water_jug_problem(x_capacity, y_capacity, target):
    max_states = x_capacity * y_capacity + 1
    visited = np.zeros((x_capacity + 1, y_capacity + 1), dtype=bool)
    parent = np.empty((x_capacity + 1, y_capacity + 1), dtype=object)
    q = []

    # Initialize the queue with the initial state (0, 0)
    q.append((0, 0))
    visited[0][0] = True

    while q:
        current_state = q.pop(0)
        x, y = current_state

        if x == target or y == target:
            # Goal state reached, reconstruct and print the path
            path = []
            while current_state != (0, 0):
                path.append(current_state)
                current_state = parent[current_state[0]][current_state[1]]
            path.append((0, 0))
            path.reverse()
            for state in path:
                print(f"({state[0]}, {state[1]})")
            return

        # Fill jug x
        if x < x_capacity and not visited[x_capacity][y]:
            q.append((x_capacity, y))
            visited[x_capacity][y] = True
            parent[x_capacity][y] = current_state

        # Fill jug y
        if y < y_capacity and not visited[x][y_capacity]:
            q.append((x, y_capacity))
            visited[x][y_capacity] = True
            parent[x][y_capacity] = current_state

        # Empty jug x
        if x > 0 and not visited[0][y]:
            q.append((0, y))
            visited[0][y] = True
            parent[0][y] = current_state

        # Empty jug y
        if y > 0 and not visited[x][0]:
            q.append((x, 0))
            visited[x][0] = True
            parent[x][0] = current_state

        # Pour water from x to y
        if x > 0 and y < y_capacity:
            pour = min(x, y_capacity - y)
            new_state = (x - pour, y + pour)
            if not visited[new_state[0]][new_state[1]]:
                q.append(new_state)
                visited[new_state[0]][new_state[1]] = True
                parent[new_state[0]][new_state[1]] = current_state

        # Pour water from y to x
        if y > 0 and x < x_capacity:
            pour = min(y, x_capacity - x)
            new_state = (x + pour, y - pour)
            if not visited[new_state[0]][new_state[1]]:
                q.append(new_state)
                visited[new_state[0]][new_state[1]] = True
                parent[new_state[0]][new_state[1]] = current_state

    # If the goal state cannot be reached
    print("Goal state cannot be reached.")

if __name__ == "__main__":
    x_capacity = 4
    y_capacity = 3
    target = 2

    print("Steps to reach the goal:")
    water_jug_problem(x_capacity, y_capacity, target)

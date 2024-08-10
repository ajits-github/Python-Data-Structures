# """
# Python Data Structures - A Game-Based Approach
# A Star Algorithm maze solver.
# Uses a priority queue containing f-values and (i, j)
# # tuples along with dictionaries for predecessors and g-values.
# """

from helpers import get_path, offsets, is_legal_pos, read_maze
from priority_queue import PriorityQueue


def heuristic(a, b):
    """
    Calculates the Manhattan distance between two pairs of grid coordinates.
    """
    x1, y1 = a
    x2, y2 = b
    return abs(x1 - x2) + abs(y1 - y2)


def a_star(maze, start, goal):
    """
    A* algorithm to find the shortest path from start to goal in a maze.
    """
    pq = PriorityQueue()
    pq.put((0, start))

    g_values = {start: 0}
    predecessors = {start: None}

    while not pq.is_empty():
        current_pos = pq.get()

        if current_pos == goal:
            return get_path(predecessors, start, goal)

        for direction in offsets:
            row_offset, col_offset = offsets[direction]
            neighbor = (current_pos[0] + row_offset,
                        current_pos[1] + col_offset)

            if is_legal_pos(maze, neighbor) and neighbor not in g_values:
                new_cost = g_values[current_pos] + 1
                g_values[neighbor] = new_cost
                f_value = new_cost + heuristic(goal, neighbor)
                pq.put((f_value, neighbor))
                predecessors[neighbor] = current_pos

    return None


if __name__ == "__main__":
    # Test 1 - Simple Open Maze
    maze = [[' '] * 3 for _ in range(3)]
    start_pos = (0, 0)
    goal_pos = (2, 2)
    result = a_star(maze, start_pos, goal_pos)
    print("Test 1 result:", result)
    assert result == [(0, 0), (0, 1), (0, 2), (1, 2), (2, 2)]

    # Test 2 - Mini Maze BFS
    maze = read_maze("mazes/mini_maze_bfs.txt")
    start_pos = (0, 1)  # Start from the first open cell
    goal_pos = (2, 2)  # Goal is the bottom-right corner
    result = a_star(maze, start_pos, goal_pos)
    print("Test 2 result:", result)

    # Test 3 - Mini Maze BFS with unreachable goal
    maze = read_maze("mazes/mini_maze_bfs.txt")
    start_pos = (0, 1)
    goal_pos = (3, 3)  # Outside of the maze bounds
    result = a_star(maze, start_pos, goal_pos)
    print("Test 3 result:", result)
    assert result is None

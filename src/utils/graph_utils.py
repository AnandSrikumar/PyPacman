import heapq

def a_star(matrix, start, target, subdivs=4):
    rows, cols = len(matrix), len(matrix[0])

    def is_valid(x, y):
        """Check if all cells in the subdivs x subdivs block are valid."""
        if not (0 <= x < rows and 0 <= y < cols):
            return False
        for dx in range(subdivs*2):
            for dy in range(subdivs*2):
                if x + dx >= rows or y + dy >= cols or matrix[x + dx][y + dy] == 'wall':
                    return False
        return True

    def heuristic(a, b):
        """Calculate Manhattan distance."""
        return abs(a[0] - b[0]) + abs(a[1] - b[1])
    
    def path_builder(current, came_from):
        path = []
        while current in came_from:
            path.append(current)
            current = came_from[current]
        path.append(start)
        return path[::-1]

    # Directions: Up, Down, Left, Right
    directions = [
        (-1, 0), (1, 0), (0, -1), (0, 1)
    ]

    open_set = []
    heapq.heappush(open_set, (0, start))  # (priority, position)
    came_from = {}  # To reconstruct the path

    g_score = {start: 0}
    f_score = {start: heuristic(start, target)}
    closest_node = start
    closest_distance = heuristic(start, target)

    while open_set:
        _, current = heapq.heappop(open_set)

        if current == target:
            # Reconstruct path
            return path_builder(current, came_from) #
            

        for dx, dy in directions:
            neighbor = (current[0] + dx, current[1] + dy)

            if is_valid(neighbor[0], neighbor[1]):
                tentative_g_score = g_score[current] + 1  # All moves cost 1
                if neighbor not in g_score or tentative_g_score < g_score[neighbor]:
                    came_from[neighbor] = current
                    g_score[neighbor] = tentative_g_score
                    f_score[neighbor] = tentative_g_score + heuristic(neighbor, target)

                    if neighbor not in [pos for _, pos in open_set]:
                        heapq.heappush(open_set, (f_score[neighbor], neighbor))
                
                h_dist = heuristic(neighbor, target)
                if h_dist < closest_distance:
                    closest_node = neighbor
                    closest_distance = h_dist

    return path_builder(closest_node, came_from)  #


def compute_paths(matrix, start, target, result_queue):
    from src.utils.graph_utils import a_star  # Import here to avoid process pickling issues
    paths = a_star(matrix, start, target)
    result_queue.put(paths)
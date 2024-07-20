import heapq


def dijkstra(graph, start):
    # Initialization
    priority_queue = []
    heapq.heappush(priority_queue, (0, start))  # (distance, node)
    distances = {node: float('infinity') for node in graph}
    distances[start] = 0
    shortest_path_tree_set = set()

    while priority_queue:
        (current_distance, current_node) = heapq.heappop(priority_queue)
        
        if current_node in shortest_path_tree_set:
            continue
        
        shortest_path_tree_set.add(current_node)

        for neighbor, weight in graph[current_node].items():
            distance = current_distance + weight

            # Only consider this new path if it's shorter
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(priority_queue, (distance, neighbor))
    
    return distances

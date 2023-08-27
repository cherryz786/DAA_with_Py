def bfs(graph, start):
    visited = set()  # create a set which stores unique values to keep track of visited nodes
    queue = [start]  # Using a list for BFS traversal

    while queue:
        vertex = queue.pop(0)  # Get the next vertex from the front of the list
        if vertex not in visited:
            print(vertex, end=" ")  # Process the current vertex
            visited.add(vertex)  # Mark the vertex as visited
            queue.extend(graph[vertex] - visited)  # Add unvisited neighbors to the list


# Example graph represented as an adjacency list
graph = {
    "A": {"B", "C"},
    "B": {"A", "D", "E"},
    "C": {"A", "F"},
    "D": {"B"},
    "E": {"B", "F"},
    "F": {"C", "E"},
}

start_vertex = "A"
print("BFS traversal starting from vertex", start_vertex)
bfs(graph, start_vertex)

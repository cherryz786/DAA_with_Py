def dfs(graph, start):
    visited = set()  # Create a set which stores unique values to keep track of visited nodes
    stack = [start]  # Using the list data structure as a stack for DFS traversal 
                    # because it is easy to implement and less complex.

    while stack:    # (while an element is present in a stack)
        vertex = stack.pop()  # Get the next vertex from the stack and make it the next vertex
        if vertex not in visited:
            print(vertex, end=" ")  # Process the current vertex
            visited.add(vertex)  # Mark the vertex as visited, here we cannot use the "append"
            # because "visited is basically a set and you cannnot perform append operation
            # on a set, but you can do that on lists tho.."

            stack.extend(graph[vertex] - visited)  # Add unvisited neighbors to the stack
            # Here, we extend the stack with the neighbors of the current vertex that have not 
            # been visited yet. This ensures that these neighbors will be explored in the future.


# Example graph represented as an adjacency list
graph = {
    "A": {"B", "C"},
    "B": {"A", "D", "E"},
    "C": {"A", "F"},    # (basically a dictionary)
    "D": {"B"},
    "E": {"B", "F"},
    "F": {"C", "E"},
}

start_vertex = "A"
print("DFS traversal starting from vertex", start_vertex)
dfs(graph, start_vertex)

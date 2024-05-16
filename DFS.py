def dfs(graph, start, visited=None):
    if visited is None:
        visited = set()
    visited.add(start)
    print(start, end=" ")
    for neighbor in graph.get(start, []):
        if neighbor not in visited:
            dfs(graph, neighbor, visited)

graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F'],
    'D': ['B'],
    'E': ['B', 'F'],
    'F': ['C', 'E']
}

print("DFS starting from node 'A':")
dfs(graph, 'A')

# Theory
# 1. Definition: DFS stands for Depth-First Search. 
# 2. Traversal Strategy: It explores as far as possible along each branch before backtracking.
# 3. Exploration: It starts at a selected node and explores as deeply as possible along each branch before backtracking.
# 4. Algorithm Types: DFS can be implemented using either recursion or a stack data structure.
# 5. Visited Nodes: To avoid revisiting the same node, DFS maintains a set of visited nodes.
# 6. Applications: DFS is used for graph traversal, topological sorting, cycle detection, finding connected components, solving puzzles, and more.
# 7. Completeness: DFS may not find a solution if it gets stuck in an infinite loop or fails to explore certain branches.
# 8. Memory Efficiency: It has good memory efficiency, especially when implemented using recursion, as it only needs to store information about the current path.
# 9. Time Complexity: The time complexity of DFS is O(V + E), where V is the number of vertices and E is the number of edges in the graph.
# 10. Flexibility: DFS can be adapted for various graph-related problems due to its simplicity and versatility.

#Explanation:
# 1. `def dfs(graph, start, visited=None):`: This line defines a function called `dfs` which takes three parameters: `graph` (the graph represented as an adjacency list), `start` (the starting node for DFS traversal), and `visited` (a set to keep track of visited nodes). `visited` is set to `None` by default.
# 2. `if visited is None:`: This line checks if the `visited` set is `None`, indicating that it's the first call to the function. If it is, it initializes `visited` as an empty set.
# 3. `visited.add(start)`: This line adds the current node `start` to the `visited` set, marking it as visited.
# 4. `print(start, end=" ")`: This line prints the current node `start` with a space after it, without moving to a new line. This is for displaying the order of traversal.
# 5. `for neighbor in graph.get(start, []):`: This line iterates over the neighbors of the current node `start`. It uses `graph.get(start, [])` to get the neighbors of `start` from the adjacency list. If `start` is not found in the graph, it defaults to an empty list `[]`.
# 6. `if neighbor not in visited:`: This line checks if the neighbor node `neighbor` has not been visited yet.
# 7. `dfs(graph, neighbor, visited)`: This line recursively calls the `dfs` function with the neighbor node `neighbor` as the new starting node. It passes the `visited` set to keep track of visited nodes throughout the traversal.
# The rest of the code consists of the example graph definition and the function call to start DFS traversal from node 'A'.
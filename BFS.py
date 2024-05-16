from collections import deque

def bfs(graph, start):
    visited = set()
    queue = deque([start])
    visited.add(start)

    while queue:
        node = queue.popleft()
        print(node, end=" ")

        for neighbor in graph.get(node, []):
            if neighbor not in visited:
                queue.append(neighbor)
                visited.add(neighbor)

graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F'],
    'D': ['B'],
    'E': ['B', 'F'],
    'F': ['C', 'E']
}

print("BFS starting from node 'A':")
bfs(graph, 'A')

#Theory
# 1. Definition: BFS stands for Breadth-First Search.
# 2. Traversal Strategy: It explores all neighbor nodes at the present depth before moving on to nodes at the next depth level.
# 3. Exploration: BFS starts at a selected node and explores all its neighbors before moving on to the next level of neighbors.
# 4. Algorithm Type: BFS is implemented using a queue data structure.
# 5. Visited Nodes: Similar to DFS, BFS maintains a set of visited nodes to avoid revisiting.
# 6. Applications: BFS is used for graph traversal, shortest path finding (in unweighted graphs), connected components, network broadcasting, and more.
# 7. Completeness: BFS is guaranteed to find the shortest path between two nodes in an unweighted graph.
# 8. Memory Efficiency: It may require more memory than DFS as it needs to store information about all the nodes at the current level.
# 9. Time Complexity: The time complexity of BFS is O(V + E), where V is the number of vertices and E is the number of edges in the graph.
# 10. Flexibility: BFS is versatile and can be adapted for various graph-related problems, particularly those requiring finding the shortest path.

# Explanation:
# 1. `from collections import deque`: Imports the `deque` class from the `collections` module. Deque is used to efficiently implement queues in Python.
# 2. `def bfs(graph, start):`: Defines a function called `bfs` which takes two parameters: `graph` (the graph represented as an adjacency list) and `start` (the starting node for BFS traversal).
# 3. `visited = set()`: Initializes a set to keep track of visited nodes.
# 4. `queue = deque([start])`: Initializes a deque with the starting node `start` as the only element, representing the queue for BFS traversal.
# 5. `visited.add(start)`: Adds the starting node `start` to the visited set.
# 6. `while queue:`: Initiates a while loop that continues as long as the queue is not empty.
# 7. `node = queue.popleft()`: Retrieves and removes the leftmost (front) element from the queue, representing the current node to explore in BFS.
# 8. `print(node, end=" ")`: Prints the current node.
# 9. `for neighbor in graph.get(node, []):`: Iterates over the neighbors of the current node `node`. Uses `graph.get(node, [])` to get the neighbors of `node` from the adjacency list. If `node` is not found in the graph, it defaults to an empty list `[]`.
# 10. `if neighbor not in visited:`: Checks if the neighbor node `neighbor` has not been visited yet.
# 11. `queue.append(neighbor)`: Appends the unvisited neighbor node `neighbor` to the end of the queue for further exploration.
# 12. `visited.add(neighbor)`: Marks the neighbor node `neighbor` as visited.
# 13. The rest of the code consists of the example graph definition and the function call to start BFS traversal from node 'A'.
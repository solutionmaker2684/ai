from collections import deque

def waterJugSolverBFS(jug1, jug2, aim):
    queue = deque([(0, 0)])
    visited = set([(0, 0)])
    parents = {}

    while queue:
        current_state = queue.popleft()
        amt1, amt2 = current_state

        if amt1 == aim or amt2 == aim:
            steps = []
            while current_state != (0, 0):
                steps.append(current_state)
                current_state = parents[current_state]
            steps.append((0, 0))
            steps.reverse()
            return steps

        next_states = [
            (jug1, amt2),  
            (amt1, jug2),  
            (0, amt2),     
            (amt1, 0),     
            (min(jug1, amt1 + amt2), max(0, amt1 + amt2 - jug1)),  
            (max(0, amt1 + amt2 - jug2), min(jug2, amt1 + amt2))   
        ]

        for state in next_states:
            if state not in visited:
                queue.append(state)
                visited.add(state)
                parents[state] = current_state

    return None

jug1_capacity = 4
jug2_capacity = 3
desired_quantity = 2

solution = waterJugSolverBFS(jug1_capacity, jug2_capacity, desired_quantity)
if solution:
    print("Water Jug problem solution")
    for step in solution:
        print(step)
else:
    print("No solution found.")


#Theory
# The Water Jug problem is a classic puzzle where we're tasked with measuring a specific quantity of water using two jugs of known capacities. To solve this problem using BFS, we represent the problem as a graph, with each node representing a state of the jugs. BFS systematically explores these states, starting from the initial state and expanding to neighboring states. We maintain a queue to manage the order of exploration and a set to track visited states, ensuring efficiency. By traversing the graph in a breadth-first manner, BFS guarantees finding the shortest path to the solution, if one exists. This approach offers a systematic and efficient way to solve the Water Jug problem.

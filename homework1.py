def is_fully_connected(graph, num_nodes):
    # Step 1: Initialize the visited array with False for all nodes
    visited = [False] * num_nodes
    
    # Step 2: Define the standard DFS function
    def dfs(node):
        visited[node] = True
        # Assuming graph is represented as an adjacency list
        for neighbor in graph[node]:
            if not visited[neighbor]:
                dfs(neighbor)
                
    # Step 3: Run DFS starting from Node 0
    if num_nodes > 0:
        dfs(0)
        
    # Step 4: Iterate through the visited array
    for was_visited in visited:
        if not was_visited:
            return False  # Found an unreachable node
            
    return True  

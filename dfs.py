# Depth First Search uses STACK AND RECURSION

from collections import defaultdict

def dfs(graph, start, visited, path):
    path.append(start)
    visited[start] = True
    for neighbour in graph[start]:
        if not visited[neighbour]:
            dfs(graph, neighbour, visited, path)
            visited[neighbour] = True
    return path

# Input the number of nodes and edges
n, e = map(int, input().split())

# Create the graph
graph = defaultdict(list)
for i in range(e):
    u, v = input().split()
    graph[u].append(v)
    graph[v].append(u)

# Choose start node
start = input("Enter the start node: ")

# Perform DFS
visited = defaultdict(bool)
path = []
traversedpath = dfs(graph, start, visited, path)

# Print DFS traversal path
print(traversedpath)

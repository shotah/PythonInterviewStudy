# Using a Python dictionary to act as an adjacency list
graph = {
  '5' : ['3','7'],
  '3' : ['2', '4'],
  '7' : ['8'],
  '2' : [],
  '4' : ['8'],
  '8' : []
}

visited = []
def dfs(visited: list, graph: dict, node: str) -> list:  #function for dfs
    if node not in visited:
        visited.append(node)
        for neighbor in graph[node]:
            dfs(visited, graph, neighbor)
    return visited

# Driver Code
print("Following is the Depth-First Search")
print(
  dfs(visited, graph, '5')
)

graph = {
  '5' : ['3','7'],
  '3' : ['2', '4'],
  '7' : ['8'],
  '2' : [],
  '4' : ['8'],
  '8' : []
}

visited = [] # List for visited nodes.
queue = []     #Initialize a queue

def bfs(visited, graph, node): #function for BFS
  visited.append(node)
  queue.append(node)
  while queue:          # Creating loop to visit each node
    m = queue.pop(0)
    for neighbor in graph[m]:
      if neighbor not in visited:
        visited.append(neighbor)
        queue.append(neighbor)
  return visited

# Driver Code
print("Following is the Breadth-First Search")
print(
  bfs(visited, graph, '5')    # function calling
)

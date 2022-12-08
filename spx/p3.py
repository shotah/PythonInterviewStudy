# Roads start in A, and End in B.
# validate all B roads can path find to A
# if not? flip B road.
import json

def dfs(visited, graph, node):
    if node not in visited:
        visited.append(node)
        for neighbor in graph.get(node, []):
            dfs(visited, graph, neighbor)
    return visited

def bfs(visited, graph, node):
    visited.append(node)
    queue = [node]
    while queue:
        m = queue.pop(0)
        for neighbor in graph[m]:
            if neighbor not in visited:
                visited.append(neighbor)
                queue.append(neighbor)
    return visited

def flip_road(start, end, graph):
    for key in graph.copy():
        if end in graph[key]:
            graph[key].remove(end)
            if graph[key] == []:
                del graph[key]
            graph[end] = start
    print(
        json.dumps(graph)
    )
    return graph

def make_graph(connections):
    graph = {}
    for a, b in connections:
        if a not in graph:
            graph[a] = []
        graph[a].append(b)
    return graph

def solution(a, b):
    hospital = 0
    flipped_road_counter = 0
    # graph out all the roads:
    graph = make_graph(zip(a, b))
    print(json.dumps(graph))
    
    # Work through graph to validate roads connect to hospital
    for key in graph.copy():
        for dest in graph[key]:
            visited = []
            attempts = 0
            while hospital not in visited and attempts <= 3:
                attempts += 1
                # use dfs to validate connection:
                visited = dfs(visited, graph, dest)
                if hospital not in visited:
                    print(key, visited[-1])
                    graph = flip_road(key, visited[-1], graph)
                    print(
                        json.dumps(graph)
                    )
                # TODO: Attempt to flip road and try again
                # {"0": [1], "2": [1, 4], "3": [4]}
                # SUCCESS update graph and add it to road counter




a = [0,2,2,3]
b = [1,1,4,4]
# should return 2
s = solution(a,b)
print(s)



# We'd love to hear your feedback about one of the tasks you've just solved: 
# "Given a directed tree count how many edges one has to reorient to make the root reachable from every node."
# Given a directed tree count how many edges one has to reorient to make the root reachable from every node.

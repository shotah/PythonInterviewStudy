# Roads start in A, and End in B.
# validate all B roads can path find to A
# if not? flip B road.


# {"0": [1], "2": [1, 4], "3": [4]}

def build_graph(a,b, count_of_roads_to_flip):
    graph = {}
    path = []
    # iterate through coordinates 
    for i in zip(a, b):
        # if zero do some always flip them to hospital
        if i[0] == 0:
            path.append([i[1], i[0]])
            # many regrets with the graph logic
            if i[1] not in graph:
                graph[i[1]] = [i[0]]
            else:
                graph[i[1]].append(i[0])
            # count that we flipped the road
            count_of_roads_to_flip += 1
        else:
            # append to path and add to graph
            path.append(list(i))
            if i[0] not in graph:
                graph[i[0]] = [i[1]]
            else:
                graph[i[0]].append(i[1])    

def dfs(visited, graph, node):
    if node not in visited:
        visited.append(node)
        for neighbor in graph.get(node, []):
            dfs(visited, graph, neighbor)
    return visited

def solution(a, b):
    count_of_roads_to_flip = 0
    hospital = 0
    


    # Sort and start with the shortest roads first.
    path = sorted(path, key=lambda k: [k[1], k[0]], reverse=False)
    # Validate that each road can get to the hospital
    for road in path:
        road_to_validate = road[1]
        # if it is the hospital or connected go to next road
        if road_to_validate == 0 or road[0] == 0: continue

        # use dfs to see if we connect to the hospital
        visited = []
        attempts = 0
        while attempts <= len(a) and hospital not in visited:
            attempts += 1
            visited = []
            visited = dfs(visited, graph, road_to_validate)
            print(visited)
            print(road)
    # return the count of the roads we flipped
    return count_of_roads_to_flip


a = [0,2,2,3]
b = [1,1,4,4]
# should return 2
s = solution(a,b)
print(s)

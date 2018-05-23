
import math
import time

#Standard 4 Node Graph
'''
graph = {}
graph["start"] = {}
graph["start"]["a"] = 6
graph["start"]["b"] = 2
graph["a"] = {}
graph["a"]["end"] = 1
graph["b"] = {}
graph["b"]["a"] = 3
graph["b"]["end"] = 5
graph["end"] = {}
'''

#With Negative
'''
graph = {}
graph["start"] = {}
graph["start"]["a"] = 2
graph["start"]["b"] = 2
graph["a"] = {}
graph["a"]["c"] = 2
graph["a"]["end"] = 2
graph["b"] = {}
graph["b"]["a"] = 2
graph["c"] = {}
graph["c"]["b"] = -1
graph["c"]["end"] = 2
graph["end"] = {}
'''

graph = {}
graph["start"] = {}
graph["start"]["a"] = 4
graph["start"]["h"] = 2
graph["start"]["e"] = 4

graph["a"] = {}
graph["a"]["b"] = 2
graph["a"]["start"] = 4

graph["h"] = {}
graph["h"]["start"] = 2
graph["h"]["g"] = 2

graph["g"] = {}
graph["g"]["h"] = 2
graph["g"]["f"] = 6

graph["f"] = {}
graph["f"]["g"] = 6
graph["f"]["e"] = 2

graph["e"] = {}
graph["e"]["f"] = 2
graph["e"]["d"] = 2

graph["d"] = {}
graph["d"]["e"] = 2
graph["d"]["c"] = 2
graph["d"]["goal"] = 2

graph["c"] = {}
graph["c"]["d"] = 2
graph["c"]["b"] = 2

graph["b"] = {}
graph["g"]["a"] = 2
graph["g"]["c"] = 2

graph["goal"] = {}

heuristic = {'start': 8 , 'a': 4 , 'b': 2, 'c': 4, 'd': 2, 'e': 4, 'f': 6, 'g': 12, 'h': 10, 'goal': 0}


def dijkstra(graph, start, end):
    cost = {}
    parent = {}
    NotVisited = graph
    
    infinity = math.inf

    for node in graph:
        cost[node] = infinity
    cost[start] = heuristic[start]

    while NotVisited:
        
        minNode = None
        for node in NotVisited:
            if minNode == None:
                minNode = node
            elif cost[node] < cost[minNode]:
                minNode = node

        if minNode == end:
            break 

        for child, weight in graph[minNode].items():
            if weight + cost[minNode] - heuristic[minNode] + heuristic[child] < cost[child]:
                cost[child] = weight + cost[minNode] - heuristic[minNode] + heuristic[child]
                parent[child] = minNode
                
        NotVisited.pop(minNode)

    currentNode = end
    path = []
    print(cost)
    print(parent)
    while currentNode != start:
        try:
            path.append(parent[currentNode])
            currentNode = parent[currentNode]
        except:
            print('Not Possible To Go That Way')

    finalPath = []
    for value in reversed(path):
        finalPath.append(value)

    finalPath.append(end)


    print('The Path from', start, 'to', end, 'is' , finalPath)

    
        
            

    
        
    
    

dijkstra(graph, 'start', 'goal')

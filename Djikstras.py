
import math
import time

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

def dijkstra(graph, start, end):
    cost = {}
    parent = {}
    NotVisited = graph
    
    infinity = math.inf

    for node in graph:
        cost[node] = infinity
    cost[start] = 0

    while NotVisited:
        
        minNode = None
        for node in NotVisited:
            if minNode == None:
                minNode = node
            elif cost[node] > cost[minNode]:
                minNode = node

        for child, weight in graph[minNode].items():
            if weight + cost[minNode] < cost[child]:
                cost[child] = weight + cost[minNode]
                parent[child] = minNode
                
        NotVisited.pop(minNode)

    currentNode = end
    path = []
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

    
        
            

    
        
    
    

dijkstra(graph, 'start', 'end')

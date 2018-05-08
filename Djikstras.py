
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
graph["start"]["a"] = 2
graph["start"]["d"] = 1
graph["a"] = {}
graph["a"]["c"] = 3
graph["a"]["b"] = 5
graph["a"]["start"] = 2

graph["d"] = {}
graph["d"]["e"]
graph["d"]["start"] = 1

graph["e"] = {}
graph["e"]["c"] = 3
graph["e"]["d"] = 2

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
            elif cost[node] < cost[minNode]:
                minNode = node

        for child, weight in graph[minNode].items():
            if weight + cost[minNode] < cost[child]:
                cost[child] = weight + cost[minNode]
                parent[child] = minNode
                
        NotVisited.pop(minNode)

    currentNode = end
    path = []
    print(cost)
    print(parent)
    time.sleep(10)
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

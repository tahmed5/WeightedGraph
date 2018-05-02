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


order = ['start','a','b','end']

cost = {}

'''
for node in order:
    if node == 'start':
        cost[node] = 0

    for key in graph[node]:
        print('KEY', key)
        print('GRAPH[NODE]', graph[node])
        if key in cost.keys():
            if cost[key] < graph[node][key]: 
                cost[key] = graph[node][key]
            print('COST[KEY]',cost[key])
            print('GRAPH[NODE][KEY]', graph[node][key])
            print('COST',cost)

        if key not in cost.keys():
            cost[key] = graph[node][key]
        
    for node in graph:
        if node not in cost.keys():
            cost[node] = math.inf

    input()

'''

processed = []
processed.append('start')

cost = {}

cost['a'] = 6
cost['b'] = 2
cost['end'] = math.inf

parents = {}

parents["a"] = "start"
parents["b"] = "start"
parents["end"] = None

node = min(graph[order[0]], key = graph[order[0]].get)


def update_cost(node):
    print(node)
    input()
    neighbours = graph[node]
    for n in neighbours.keys():
        currentNodeCost = cost[node]
        newCost = currentNodeCost + graph[node][n]
        oldCost = cost[n]
        if newCost < oldCost:
            cost[n] = newCost
            parents[n] = node
    processed.append(node)

for c in cost.keys():
    if c not in processed:
        print(c)
        update_cost(c)
        
print(cost)
print(parents)




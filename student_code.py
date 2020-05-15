import math

def dist(graph, n1, n2):
    n_one = graph.intersections[n1]
    n_two = graph.intersections[n2]
    a = n_one[0] - n_two[0]
    b = n_one[1] - n_two[1]
    dist = math.sqrt((a ** 2) + (b**2))
    return dist

def shortest_path(graph, start, goal):
    fr = set()
    prev = set()
    gcost = {}
    fcost = {}
    parent = {}
    
    curr = start
    fr.add(curr)
    gcost[curr] = 0
    fcost[curr] = gcost[curr] + dist(graph, start, goal)
    parent[curr] = None
    
    while fr:
        curr = min(fr, key=lambda x:fcost[x])
        
        if curr == goal:
            p = []
            while parent[curr]:
                p.insert(0, curr)
                curr = parent[curr]
            p.insert(0, curr)
            return p
        
        fr.remove(curr)
        prev.add(curr)
        for n in graph.roads[curr]:
            if n in prev:
                continue

            if n not in fr:
                fr.add(n)
                gcost[n] = gcost[curr] + dist(graph,n,curr)
                fcost[n] = gcost[n] + dist(graph, n, goal)
                parent[n] = curr
            
            ngcost = gcost[curr] + dist(graph, n, curr)

            if gcost[n] > ngcost:
                gcost[n] = ngcost
                fcost[n] = gcost[n] + dist(graph, n, goal)
                parent[n] = curr
from collections import defaultdict
import sys
sys.setrecursionlimit(10**6) 


n, m = map(int,input().split())

roads = [
    tuple(map(int,input().split())) for i in range(m)
]

graph = defaultdict(list)
for a, b in roads:
    graph[a].append(b)
    graph[b].append(a)


visited = [False] * (n + 1)
parent = [None] * (n + 1)
path = []

def dfs(node):
    visited[node] = True
    path.append(node)

    for neighbor in graph[node]:
        if not visited[neighbor]:
            parent[neighbor] = node
            cycle = dfs(neighbor)
            if cycle is not None:
                return cycle
        elif neighbor != parent[node]: 
            cycle = [neighbor]
            i = len(path) - 1
            while path[i] != neighbor:
                cycle.append(path[i])
                i -= 1
            cycle.append(neighbor)
            cycle.reverse()
            return cycle

    path.pop() # Remove the current node from the path before backtracking
    return None

# Call the DFS function starting from each unvisited node
flag = True
for node in range(1, n + 1):
    if not visited[node]:
        cycle = dfs(node)
        if cycle is not None:
            print(len(cycle))
            print(*cycle)
            flag = False
            break

if(flag):
    print("IMPOSSIBLE")
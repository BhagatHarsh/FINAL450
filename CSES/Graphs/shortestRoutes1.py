import heapq

def dijkstra(graph, start):
    n = len(graph)
    dist = [float('inf')] * n
    dist[start] = 0
    visited = [False] * n
    queue = [(0, start)]

    while queue:
        d, node = heapq.heappop(queue)
        if visited[node]:
            continue
        visited[node] = True
        for neighbor, weight in graph[node]:
            if dist[node] + weight < dist[neighbor]:
                dist[neighbor] = dist[node] + weight
                heapq.heappush(queue, (dist[neighbor], neighbor))

    return dist

n, m = map(int,input().split())
graph = [[] for _ in range(n+1)]
for _ in range(m):
    x, y, z = map(int,input().split())
    graph[x].append((y, z))

distances = dijkstra(graph, 1)
for i in range(1, n+1):
    print(distances[i], end=' ')
print()

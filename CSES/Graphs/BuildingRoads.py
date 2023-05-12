def kosaraju(graph):
    # Step 1: Create an empty stack and mark all vertices as not visited
    stack = [i for i in range(len(graph))]
    visited = [False] * len(graph)

    def dfs_iterative(start):
        component = []
        stack = [start]
        while stack:
            node = stack.pop()
            if not visited[node]:
                visited[node] = True
                component.append(node)
                for neighbor in graph[node]:
                    if not visited[neighbor]:
                        stack.append(neighbor)
        return component

    # Step -1: Find the strongly connected components
    strongly_connected_components = []
    while stack:
        node = stack.pop()
        if not visited[node]:
            component = dfs_iterative(node)
            strongly_connected_components.append(component)
            # print("Stack:", stack)
            # print("Strongly Connected Components:", strongly_connected_components)

    return strongly_connected_components



n, m = map(int,input().split())
roads = [
    tuple(map(int,input().split())) for i in range(m)
]
G = [[] for i in range(n)]

for u,v in roads:
    G[u-1].append(v-1)
    G[v-1].append(u-1)

paths = kosaraju(G)
print(len(paths)-1)
for i in range(len(paths)-1):
    print(paths[i][0] + 1, paths[i+1][0] + 1)



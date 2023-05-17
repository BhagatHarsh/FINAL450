from collections import defaultdict, deque

n, m = map(int,input().split())

roads = [
    tuple(map(int,input().split())) for i in range(m)
]

graph = defaultdict(list)
for a, b in roads:
    graph[a].append(b)
    graph[b].append(a)


bfs = deque()
vis = [0 for i in range(n+1)]
flag = 1
for i in range(1,n+1):
    if(not vis[i]):
        bfs.append(i)
        vis[i] = 1
        while(bfs):
            ele = bfs.popleft()
            for i in graph[ele]:
                if(not vis[i]):
                    bfs.append(i)
                    if(vis[ele] == 1):
                        vis[i] = 2
                    else:
                        vis[i] = 1
                else:
                    if(vis[i] == vis[ele]):
                        flag = 0

if(flag):
    print(*vis[1:])
else:
    print("IMPOSSIBLE")
        
                




# def graph_coloring(n, edges):
    # Build the graph
    # graph = defaultdict(list)
    # for a, b in edges:
    #     graph[a].append(b)
    #     graph[b].append(a)

    # # Initialize the colors dictionary
    # colors = {i: None for i in range(1, n+1)}

#     # Color the nodes
#     for node in range(1, n+1):
#         # Check if the node has already been colored
#         if colors[node] is None:
#             # Initialize the color of the node to 1
#             colors[node] = 1
#             # Color the adjacent nodes with a different color
#             for neighbor in graph[node]:
#                 if colors[neighbor] is None:
#                     colors[neighbor] = 2
#                 elif colors[neighbor] == colors[node]:
#                     # It is not possible to color the graph with only two colors
#                     return None

#     # Return the colors of the nodes
#     return list(colors.values())

# def divide_pupils(n, friendships):
#     # Create an adjacency list representation of the graph
#     graph = defaultdict(list)
#     for i, j in friendships:
#         graph[i].append(j)
#         graph[j].append(i)

#     # Initialize an empty dictionary to store the color of each node
#     colors = {}

#     # Define a recursive function to color the nodes
#     def color_node(node, color):
#         colors[node] = color
#         for neighbor in graph[node]:
#             if neighbor not in colors:
#                 color_node(neighbor, 1 - color)
#             elif colors[neighbor] == color:
#                 return False
#         return True

#     # Color each node in the graph
#     for node in range(1, n+1):
#         if node not in colors:
#             if not color_node(node, 0):
#                 return []

#     splitG = []
#     for node in graph:
#         if(colors[node]):
#             splitG.append(2)
#         else:
#             splitG.append(1)
#     return splitG




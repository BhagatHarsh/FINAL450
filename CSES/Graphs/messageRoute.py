from collections import deque

n, m = map(int,input().split())
route = [
    tuple(map(int,input().split())) for i in range(m)
]

G = [[] for i in range(n+1)]
vis = [False for i in range(n+1)]
par = [-1 for i in range(n+1)]

for u,v in route:
    G[u].append(v)
    G[v].append(u)

    
bfs = deque()
bfs.append(1)
vis[1] = True

while(bfs):
    ele = bfs.popleft()
    for i in G[ele]:
        if(not vis[i]):
            par[i] = ele
            vis[i] = True
            bfs.append(i)

if(vis[n]):
    minPath = [n]
    i = par[n]
    while(i != -1):
        minPath.append(i)
        i = par[i]
    print(len(minPath))
    print(*reversed(minPath))
else:
    print("IMPOSSIBLE")
    


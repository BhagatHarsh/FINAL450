'''
Constraints
1≤n,m≤1000

Example

Input:
5 8
########
#.A#...#
#.##.#B#
#......#
########

Output:
YES
9
LDDRRRRRU
'''

from collections import deque

n, m = map(int,input().split())
G = []
for i in range(n):
  s = input()
  G.append(list(s))
 
start = ()
end = ()
vis = [[0 for i in range(m)] for j in range(n)]
dist = [[1000000 for i in range(m)] for j in range(n)]
for i in range(n):
    for j in range(m):
        if(G[i][j] == 'A'):
            start = (i,j)
            break
        if(G[i][j] == 'B'):
            end = (i,j)
            break
bfs = deque()
bfs.append(start)
flag = 0
i,j = start
dist[i][j] = 0
while(bfs):
    i,j = bfs.pop()
    if(G[i][j] == 'B'):
        flag = 1
    if(i<0 or j<0 or i>=n or j>=m or vis[i][j] == 1 or G[i][j] == '#'):
        continue
    print(G[i][j])
    vis[i][j] = 1
    if(dist[i-1][j] > dist[i][j] + 1):
        dist[i-1][j] = dist[i][j] + 1
        bfs.append((i-1,j))
    if(dist[i][j-1] > dist[i][j] + 1):
        dist[i][j-1] = dist[i][j] + 1
        bfs.append((i,j-1))
    if(dist[i+1][j] > dist[i][j] + 1):
        dist[i+1][j] = dist[i][j] + 1
        bfs.append((i+1,j))
    if(dist[i][j+1] > dist[i][j] + 1):
        dist[i][j+1] = dist[i][j] + 1
        bfs.append((i,j+1))
        
for i in range(n):
    print(dist[i])
        
    
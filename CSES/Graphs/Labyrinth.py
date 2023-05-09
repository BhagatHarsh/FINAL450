from collections import deque

def main():
    n, m = map(int, input().split())
    G = [input() for _ in range(n)]

    start = end = None
    for i in range(n):
        for j in range(m):
            if G[i][j] == 'A':
                start = (i, j)
            elif G[i][j] == 'B':
                end = (i, j)

    vis = [[False] * m for _ in range(n)]
    dist = [[float('inf')] * m for _ in range(n)]
    parent = [[None] * m for _ in range(n)]

    dist[start[0]][start[1]] = 0
    vis[start[0]][start[1]] = True

    queue = deque([start])

    while queue:
        x, y = queue.popleft()
        for dx, dy in ((1, 0), (-1, 0), (0, 1), (0, -1)):
            nx, ny = x + dx, y + dy
            if 0 <= nx < n and 0 <= ny < m and not vis[nx][ny] and G[nx][ny] != '#':
                vis[nx][ny] = True
                dist[nx][ny] = dist[x][y] + 1
                parent[nx][ny] = (x, y)
                queue.append((nx, ny))

    if not vis[end[0]][end[1]]:
        print("NO")
        return

    path = []
    cur = end
    while cur != start:
        path.append(cur)
        cur = parent[cur[0]][cur[1]]
    path.append(start)

    path = path[::-1]
    moves = []

    for i in range(len(path) - 1):
        x, y = path[i]
        nx, ny = path[i + 1]
        if nx == x + 1:
            moves.append("D")
        elif nx == x - 1:
            moves.append("U")
        elif ny == y + 1:
            moves.append("R")
        elif ny == y - 1:
            moves.append("L")

    print("YES")
    print(len(moves))
    print("".join(moves))


if __name__ == "__main__":
    main()


# from collections import deque

# n, m = map(int,input().split())
# G = []
# for i in range(n):
#   s = input()
#   G.append(list(s))
 
# start = ()
# end = ()
# vis = [[0 for i in range(m)] for j in range(n)]
# dist = [[1000000 for i in range(m)] for j in range(n)]
# for i in range(n):
#     for j in range(m):
#         if(G[i][j] == 'A'):
#             start = (i,j)
#         elif(G[i][j] == 'B'):
#             end = (i,j)

# bfs = deque()
# bfs.append(start)
# flag = 0
# i,j = start
# dist[i][j] = 0
# while(bfs):
#     i,j = bfs.popleft()
#     if(G[i][j] == 'B'):
#         flag = 1
#     if(i<0 or j<0 or i>=n or j>=m or vis[i][j] == 1 or G[i][j] == '#'):
#         continue
#     vis[i][j] = 1
#     if i-1 >= 0 and G[i-1][j] != '' and G[i-1][j] != '#' and dist[i-1][j] is not None and dist[i-1][j] > dist[i][j] + 1:
#         dist[i-1][j] = dist[i][j] + 1
#         bfs.append((i-1, j))
#     if j-1 >= 0 and G[i][j-1] != '' and G[i][j-1] != '#' and dist[i][j-1] is not None and dist[i][j-1] > dist[i][j] + 1:
#         dist[i][j-1] = dist[i][j] + 1
#         bfs.append((i, j-1))
#     if i+1 < n and G[i+1][j] != '' and G[i+1][j] != '#' and dist[i+1][j] is not None and dist[i+1][j] > dist[i][j] + 1:
#         dist[i+1][j] = dist[i][j] + 1
#         bfs.append((i+1, j))
#     if j+1 < m and G[i][j+1] != '' and G[i][j+1] != '#' and dist[i][j+1] is not None and dist[i][j+1] > dist[i][j] + 1:
#         dist[i][j+1] = dist[i][j] + 1
#         bfs.append((i, j+1))

# if(flag):
#     ans = ""
#     i,j = end
#     while(dist[i][j]):
#         if(i-1>=0 and dist[i-1][j] < dist[i][j]):
#             i -= 1
#             ans+='D'
#         elif(i+1<n and dist[i+1][j] < dist[i][j]):
#             i += 1
#             ans+='U'
#         elif(j-1>=0 and dist[i][j-1] < dist[i][j]):
#             j -= 1
#             ans+='R'
#         elif(j+1<m and dist[i][j+1] < dist[i][j]):
#             j += 1
#             ans+='L'
#     print('YES')
#     print(len(ans))
#     print(ans[::-1])
# else:
#     print('NO')

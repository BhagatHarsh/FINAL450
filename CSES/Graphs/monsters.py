from collections import deque

def multisource_bfs(player, monsters, G, n, m):
    player_queue = deque([player])
    monster_queue = deque(monsters)
    vis = [[False] * m for _ in range(n)]
    parent = [[None] * m for _ in range(n)]

    for i in monsters:
        k, j = i
        vis[k][j] = True
    
    pi,pj = player
    vis[pi][pj] = True

    while player_queue or monster_queue:
        for loop in range(len(monster_queue)):
            x, y = monster_queue.popleft()
            for dx, dy in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                nx, ny = x + dx, y + dy
                if 0 <= nx < n and 0 <= ny < m and not vis[nx][ny] and G[nx][ny] != '#':
                    vis[nx][ny] = True
                    monster_queue.append((nx, ny))
        
        for loop in range(len(player_queue)):
            x, y = player_queue.popleft()
            for dx, dy in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                nx, ny = x + dx, y + dy
                if 0 <= nx < n and 0 <= ny < m and not vis[nx][ny] and G[nx][ny] != '#':
                    vis[nx][ny] = True
                    parent[nx][ny] = (x, y)
                    player_queue.append((nx, ny))

                    if nx == 0 or nx == n - 1 or ny == 0 or ny == m - 1:
                        path = []
                        while parent[nx][ny]:
                            path.append((nx, ny))
                            nx, ny = parent[nx][ny]
                        return path
    return None

n, m = map(int, input().split())
G = [input() for _ in range(n)]

player = None
monsters = []
for i in range(n):
    for j in range(m):
        if G[i][j] == 'A':
            player = (i, j)
        if G[i][j] == 'M':
            monsters.append((i, j))

nx, ny = player
if nx == 0 or nx == n - 1 or ny == 0 or ny == m - 1:
    print("YES")
    print(0)
    exit()
    

path = multisource_bfs(player, monsters, G, n, m)
if path != None:
    moves = []
    path = path + [player]
    # print(path)
    for i in range(len(path) - 1):
        x, y = path[i]
        nx, ny = path[i + 1]
        if nx == x + 1:
            moves.append("U")
        elif nx == x - 1:
            moves.append("D")
        elif ny == y + 1:
            moves.append("L")
        elif ny == y - 1:
            moves.append("R")

    print("YES")
    print(len(moves))
    print(("".join(moves))[::-1])
else:
    print("NO")






def dfs(i:int, j:int, G:list):
    stack = [(i, j)]
    while stack:
        i, j = stack.pop()
        if i < 0 or j < 0 or i >= len(G) or j >= len(G[0]):
            continue
        if G[i][j] == '#':
            continue
        G[i][j] = '#'
        stack.append((i+1, j))
        stack.append((i, j+1))
        stack.append((i-1, j))
        stack.append((i, j-1))
 
 
n, m = map(int,input().split())
# l = list(map(int,input().split()))
G = []
for i in range(n):
  s = input()
  print(s)
  print(list(s))
  G.append(list(s))
 
count = 0
for i in range(n):
  for j in range(m):
    if(G[i][j] == '.'):
      dfs(i,j,G)
      count+=1
 
print(count)
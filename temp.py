from math import ceil

n, k = map(int, input().split())
l = []
m = {}
ans = 0

for i in range(n):
    l.append(int(input()))

for i in l:
    try:
        m[i] += 1
    except:
        m[i] = 1

for i in m:
    if (m[i] % 2 == 0):
        ans += m[i]
    else:
        ans += m[i] - 1

print(ans + (ceil(n / 2) - ans // 2))

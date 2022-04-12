n = int(input())
l = list(map(int, input().split(' ')))
positives = []
for i in l:
    if(i>=0):
        positives.append(i)
    else:
        print(i,end=" ")
print(*positives)
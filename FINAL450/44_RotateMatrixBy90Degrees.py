# Link: https://www.geeksforgeeks.org/rotate-a-matrix-by-90-degree-in-clockwise-direction-without-using-any-extra-space/
for loop in range(int(input())):
    n, m = map(int, input().split())
    mat = []

    # Input the matrix
    for i in range(n):
        mat.append(list(map(int, input().split())))

    # rotate diagonally
    for i in range(n):
        for j in range(i):
            mat[i][j], mat[j][i] = mat[j][i], mat[i][j]

    # rotate along the centre column
    for i in range(n):
        for j in range(m // 2):
            mat[i][j], mat[i][-(j + 1)] = mat[i][-(j + 1)], mat[i][j]

    # printing the rotated matrix
    for i in range(n):
        print(*mat[i])

# link: https://practice.geeksforgeeks.org/problems/spirally-traversing-a-matrix/0

#User function Template for python3


class Solution:

    #Function to return a list of integers denoting spiral traversal of matrix.

    # reference: https://www.geeksforgeeks.org/print-a-given-matrix-in-spiral-form/
    def spirallyTraverse(self, ll, r, c):
        ans = []

        if (len(matrix) == 0):
            return ans

        m = len(matrix)
        n = len(matrix[0])
        seen = [[0 for i in range(n)] for j in range(m)]
        dr = [0, 1, 0, -1]
        dc = [1, 0, -1, 0]
        x = 0
        y = 0
        di = 0

        # Iterate from 0 to R * C - 1
        for i in range(m * n):
            ans.append(matrix[x][y])
            seen[x][y] = True
            cr = x + dr[di]
            cc = y + dc[di]

            if (0 <= cr and cr < m and 0 <= cc and cc < n
                    and not (seen[cr][cc])):
                x = cr
                y = cc
            else:
                di = (di + 1) % 4
                x += dr[di]
                y += dc[di]
        return ans


#{
# Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        r, c = map(int, input().strip().split())
        values = list(map(int, input().strip().split()))
        k = 0
        matrix = []
        for i in range(r):
            row = []
            for j in range(c):
                row.append(values[k])
                k += 1
            matrix.append(row)
        obj = Solution()
        ans = obj.spirallyTraverse(matrix, r, c)
        for i in ans:
            print(i, end=" ")
        print()

# } Driver Code Ends

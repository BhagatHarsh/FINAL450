#User function Template for python3
'''
Working solution from the comments
'''
#User function Template for python3


class Solution:

    def nearestSmallestTower(self, arr):
        INF = float('inf')
        n = len(arr)
        left, right = [INF] * n, [INF] * n

        stack = []
        for i in range(n):
            while stack and arr[stack[-1]] > arr[i]:
                idx = stack.pop()
                left[idx] = i
            stack.append(i)

        stack.clear()
        for i in range(n - 1, -1, -1):
            while stack and arr[stack[-1]] > arr[i]:
                idx = stack.pop()
                right[idx] = i
            stack.append(i)

        ans = []
        for i in range(n):
            if left[i] == INF and right[i] == INF:
                ans.append(-1)
            else:
                if abs(left[i] - i) < abs(right[i] - i):
                    ans.append(left[i])
                elif abs(left[i] - i) > abs(right[i] - i):
                    ans.append(right[i])
                elif arr[left[i]] >= arr[right[i]]:
                    ans.append(right[i])
                else:
                    ans.append(left[i])
        return ans


'''
My attempt didnt work
'''


class Solution:

    def nearestSmallestTower(self, arr):
        ans = []
        n = len(arr)
        if (n == 2):
            if (arr[0] < arr[1]):
                ans.append(-1)
                ans.append(0)
            elif (arr[1] < arr[0]):
                ans.append(1)
                ans.append(-1)
            else:
                ans.append(-1)
                ans.append(-1)
            return ans
        i = 1
        j = n - 1
        while (i < j):
            if (arr[i] < arr[0]):
                ans.append(i)
                break
            i += 1
        if (len(ans) == 0):
            ans.append(-1)
        for k in range(1, n - 1):
            i = k - 1
            j = k + 1
            ansi = i
            ansj = j
            while (i >= 0):
                if (arr[i] < arr[k]):
                    ansi = i
                    break
                i -= 1
            while (j < n):
                if (arr[j] < arr[k]):
                    ansj = j
                    break
                j += 1
            i = ansi
            j = ansj
            # print(k,arr[k],i,j,arr[i],arr[j])
            if (arr[i] < arr[k] or arr[j] < arr[k]):
                if (arr[j] < arr[i]):
                    ans.append(j)
                else:
                    ans.append(i)
            else:
                ans.append(-1)
        i = n - 2
        while (i >= 0):
            if (arr[i] < arr[n - 1]):
                ans.append(i)
                break
            i -= 1
        if (len(ans) != n):
            ans.append(-1)
        return ans

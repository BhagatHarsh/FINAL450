#https://practice.geeksforgeeks.org/problems/1a4b617b70f0142a5c2b454e6fbe1b9a69ce7861/1
# potd 26 Feb 2023

import collections
from collections import deque
from collections import defaultdict


def dfs(s, visit):
    ans = [s]
    visit.add(s)
    for ele in adj[s]:
        if ele not in visit:
            s = dfs(ele, visit)
            for i in s:
                ans.append(i)
    return ans


class Solution:

    def findNumberOfGoodComponent(self, V, adj):
        res = 0
        visit = set()
        for i in range(1, len(adj)):
            if i not in visit:
                ans = dfs(i, visit)
                for x in ans:
                    if len(adj[x]) != len(ans) - 1:
                        break
                else:
                    res += 1
        return res


#{
# Driver Code Starts
#Initial Template for Python 3

from sys import stdin, stdout
if __name__ == '__main__':
    test_cases = int(input())
    for _ in range(test_cases):
        E, V = map(int, input().split())
        adj = [[] for _ in range(V + 1)]
        for _ in range(E):
            a, b = map(int, input().split())
            adj[a].append(b)
            adj[b].append(a)

        res = Solution().findNumberOfGoodComponent(V, adj)
        print(res)
# } Driver Code Ends

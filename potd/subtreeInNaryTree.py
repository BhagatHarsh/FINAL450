'''
https://practice.geeksforgeeks.org/problems/079dee7e7db7a784ed73f604e3cf1712432edf79/1
'''
from collections import Counter


class Solution:

    def duplicateSubtreeNaryTree(self, root):
        global c
        c = Counter()

        def dfs(n):
            if not n:
                return "#"
            key = "{0} {1}".format(n.key,
                                   " ".join(dfs(nxt) for nxt in n.children))
            c[key] += 1
            return key

        dfs(root)
        # print(c)
        return sum(v > 1 for v in c.values())


#{
# Driver Code Starts
#Initial Template for Python 3

from collections import defaultdict
from collections import deque


class NodeNotFoundException(Exception):

    def __init__(self, value):
        self.value = value

    def __str__(self):
        return repr(self.value)


class Node:

    def __init__(self, key, children=None):
        self.key = key
        self.children = children or []

    def __str__(self):
        return str(self.key)


class N_ary_Tree:

    def __init__(self):
        self.root = None
        self.size = 0

    def find_node(self, node, key):
        if node == None or node.key == key:
            return node
        for child in node.children:
            return_node = self.find_node(child, key)
            if return_node:
                return return_node
        return None

    def add(self, new_key, parent_key=None):
        new_node = Node(new_key)
        if parent_key == None:
            self.root = new_node
            self.size = 1
        else:
            parent_key.children.append(new_node)
            self.size += 1
        return new_node


if __name__ == '__main__':
    test_cases = int(input())
    for _ in range(test_cases):

        N = [el for el in input().split()]
        '''
        N-ary Tree Building
        '''

        tree = N_ary_Tree()
        curr = 0
        for i in range(len(N)):
            if i == 0:
                q = deque()
                curr = tree.add(int(N[0]))
            elif N[i] == " " or N == "\n":
                continue
            elif q and N[i] == "N":
                curr = q.popleft()
            elif N[i] != "N":
                q.append(tree.add(int(N[i]), curr))

        res = Solution().duplicateSubtreeNaryTree(tree.root)
        print(res)
# } Driver Code Ends

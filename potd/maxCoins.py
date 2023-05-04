'''
https://practice.geeksforgeeks.org/problems/111fb97b983399c0ee9f34b7bae18ac76bf6f07a/1
'''
from typing import List
from bisect import bisect_left
from math import inf


class Solution:

    def maxCoins(self, n: int, ranges: List[List[int]]) -> int:
        ranges.sort(key=lambda x: (x[1], x[0], x[2]))
        end = [(0, 0)]
        res = 0
        for si, ei, ci in ranges:
            j = bisect_left(end, (si, inf)) - 1
            ej, cj = end[j]
            res = max(res, ci + cj)
            end.append((ei, max(ci, end[-1][1])))
        return res

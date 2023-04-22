'''
link:
https://practice.geeksforgeeks.org/problems/5877fde1c8e1029658845cd4bc94066ac1d4b09b/1
'''

from collections import Counter
from typing import List


class Solution:

    def smallerSum(self, n: int, arr: List[int]) -> List[int]:

        arrs = sorted(arr, reverse=True)
        dictarr = dict(Counter(arrs))
        setarr = sorted(dictarr.items(), key=lambda x: x[0], reverse=True)
        sarr = [0] * n
        total = sum(arr)
        diff = dict()

        for i in range(len(setarr)):
            total -= setarr[i][0] * setarr[i][1]
            diff[setarr[i][0]] = total

        for i in range(n):

            sarr[i] = diff[arr[i]]

        return (sarr)


#{
# Driver Code Starts
class IntArray:

    def __init__(self) -> None:
        pass

    def Input(self, n):
        arr = [int(i) for i in input().strip().split()]  #array input
        return arr

    def Print(self, arr):
        for i in arr:
            print(i, end=" ")
        print()


if __name__ == "__main__":
    t = int(input())
    for _ in range(t):

        n = int(input())

        arr = IntArray().Input(n)

        obj = Solution()
        res = obj.smallerSum(n, arr)

        IntArray().Print(res)

# } Driver Code Ends

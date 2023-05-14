'''
https://practice.geeksforgeeks.org/problems/e047b92794316450814b29de56cc9c6ec18371b7/1
'''

from typing import List

class Solution:
    def findMaxSubsetSum(self, N : int, A : List[int]) -> int:
        dp = [[None]*2 for _ in range(N)]
        dp[0] = [A[0], 0]
        for idx in range(1, N):
            dp[idx][1] = dp[idx-1][0]
            dp[idx][0] = max(dp[idx-1]) + A[idx]
        # print(dp)
        return max(dp[N-1])

        


#{ 
 # Driver Code Starts

class IntArray:
    def __init__(self) -> None:
        pass
    def Input(self,n):
        arr=[int(i) for i in input().strip().split()]#array input
        return arr
    def Print(self,arr):
        for i in arr:
            print(i,end=" ")
        print()


if __name__=="__main__":
    t = int(input())
    for _ in range(t):
        
        N = int(input())
        
        
        A=IntArray().Input(N)
        
        obj = Solution()
        res = obj.findMaxSubsetSum(N, A)
        
        print(res)
        

# } Driver Code Ends
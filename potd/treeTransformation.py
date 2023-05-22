'''
https://practice.geeksforgeeks.org/problems/fbcd1787378ed396a8f24b47872cbc0ad2624f1d/1
'''
from typing import List


class Solution:
    def solve(self, N : int, p : List[int]) -> int:
        if(N <= 2):
            return 0
        m = {}
        maxi = 0
        for i in range(1,N):
            try:
                m[p[i]]+=1
            except:
                m[p[i]]=1
                
            try:
                m[i]+=1
            except:
                m[i]=1
        
        return sum([1 if m[i] != 1 else 0 for i in m]) - 1
        
        
        
        



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
        
        
        p=IntArray().Input(N)
        
        obj = Solution()
        res = obj.solve(N, p)
        
        print(res)
        

# } Driver Code Ends

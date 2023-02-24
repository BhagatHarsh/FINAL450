
# link: https://practice.geeksforgeeks.org/problems/sorted-matrix/0

#User function Template for python3

class Solution:
    def sortedMatrix(self,N,Mat):
        tempo = []
        for i in range(N):
            tempo.extend(Mat[i])
        
        tempo.sort()
        ans = []
        val = 0
        for i in range(N):
            temp = []
            for j in range(N):
                temp.append(tempo[val])
                val+=1
            ans.append(temp)
        
        return ans

#{ 
 # Driver Code Starts
#Initial Template for Python 3

import math
        
if __name__=='__main__':
    t=int(input())
    for _ in range(t):
        N=int(input())
        v=[]
        for i in range(N):
            a=list(map(int,input().strip().split()))
            v.append(a)
        ob=Solution()
        ans=ob.sortedMatrix(N,v)
        for i in range(N):
            for j in range(N):
                print(ans[i][j],end=" ")
            print()
# } Driver Code Ends
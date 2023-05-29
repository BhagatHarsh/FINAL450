'''
https://practice.geeksforgeeks.org/problems/camelcase-pattern-matching2259/1
'''

class Solution:
    def CamelCase(self,N,Dictionary,Pattern):
        ans = []
        for i in Dictionary:
            cap = ""
            # print(i)
            for j in i:
                if(j.isupper()):
                    cap+=j
            # print(cap)
            if(cap.startswith(Pattern)):
                ans.append(i)
        if(len(ans) == 0):
            ans.append(-1)
        return ans

#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__=='__main__':
    t=int(input())
    for _ in range(t):
        N=int(input())
        Dictionary=list(map(str,input().split()))
        Pattern=input()
        ob=Solution()
        ans=ob.CamelCase(N,Dictionary,Pattern)
        ans.sort()
        for i in ans:
            print(i,end=" ")
        print()    
# } Driver Code Ends

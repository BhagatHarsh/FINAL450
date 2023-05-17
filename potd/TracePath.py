'''
https://practice.geeksforgeeks.org/problems/trace-path3840/1
'''

class Solution:
    def isPossible(self, n, m, s):
        l=r=u=d=0
        lr=0
        ud=0
        for i in s:
            if i=='L':
                lr-=1
                if lr<l:
                    l=lr
            if i=='R':
                lr+=1
                if lr>r:
                    r=lr
            if i=='U':
                ud+=1
                if ud>u:
                    u=ud
            if i=='D':
                ud-=1
                if ud<d:
                    d=ud
        
        if r-l+1>m or u-d+1>n:
            return 0
        else:
            return 1
    # def isPossible(self, n, m, s):
        # for ii in range(n):
        #     for j in range(m):
        #         eff = [ii,j]
        #         for i in s:
        #             if(i == 'L'):
        #                 eff[1]-=1
        #             elif(i == 'R'):
        #                 eff[1]+=1
        #             elif(i == 'U'):
        #                 eff[0]-=1
        #             else:
        #                 eff[0]+=1
        #         if(1<=eff[0]<=n and 1<=eff[1]<=m):
        #                 return 1
        # return 0


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        n, m = [int(x) for x in input().split()]
        s = input()
        
        ob = Solution()
        print(ob.isPossible(n, m, s))
# } Driver Code Ends
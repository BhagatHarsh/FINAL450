
#link: https://practice.geeksforgeeks.org/problems/common-elements1132/1

'''
Never did i thought that this lame version would work
'''

class Solution:
    def commonElements (self,A, B, C, n1, n2, n3):
        ma,mb,mc,ans = {},{},{},{}
        for i in A:
            try:
                ma[i]+=1
            except:
                ma[i]=1
        for i in B:
            try:
                mb[i]+=1
            except:
                mb[i] = 1
        for i in C:
            try:
                mc[i]+=1
            except:
                mc[i] = 1
                
        for i in ma:
            try:
                ans[i]+=1
            except:
                ans[i]=1
        for i in mb:
            try:
                ans[i]+=1
            except:
                ans[i]=1
        for i in mc:
            try:
                ans[i]+=1
            except:
                ans[i]=1
                
        dups = []
        for i in ans:
            if(ans[i] == 3):
                dups.append(i)
        dups.sort()
        return dups


#{ 
 # Driver Code Starts
#Initial Template for Python 3


t = int (input ())
for tc in range (t):
    n1, n2, n3 = list(map(int,input().split()))
    A = list(map(int,input().split()))
    B = list(map(int,input().split()))
    C = list(map(int,input().split()))
    
    ob = Solution()
    
    res = ob.commonElements (A, B, C, n1, n2, n3)
    
    if len (res) == 0:
        print (-1)
    else:
        for i in range (len (res)):
            print (res[i], end=" ")
        print ()

# } Driver Code Ends


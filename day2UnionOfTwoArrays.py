#User function Template for python3

class Solution:    
    #Function to return the count of number of elements in union of two arrays.
    def doUnion(self,a,n,b,m):
        a.extend(b)
        return len(set(a))
        # la = len(a)
        # lb = len(b)
        # for i in range(min(la,lb)):
        #     if(a[i] not in l):
        #         l.append(a[i])
        #     if(b[i] not in l):
        #         l.append(b[i])
        # if(la>=lb):
        #     for i in range(lb,la):
        #         if(a[i] not in l):
        #             l.append(a[i])
        # else:
        #     for i in range(la,lb):
        #         if(b[i] not in l):
        #             l.append(b[i])
        # return len(l)
        #code here

#{ 
#  Driver Code Starts
#Initial Template for Python 3

#contributed by RavinderSinghPB
if __name__=='__main__':
    t=int(input())
    for _ in range(t):
        
        n,m=[int(x) for x in input().strip().split()]
        
        a=[int(x) for x in input().strip().split()]
        b=[int(x) for x in input().strip().split()]
        ob=Solution()
        
        print(ob.doUnion(a,n,b,m))
# } Driver Code Ends
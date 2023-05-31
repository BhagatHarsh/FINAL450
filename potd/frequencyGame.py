'''
https://practice.geeksforgeeks.org/problems/frequency-game/1
'''

#User function Template for python3


def LargButMinFreq(arr,n):
    
    m = {}
    mf = 10**10
    for i in arr:
        try:
            m[i]+=1
        except:
            m[i] = 1
            
    for i in m:
        mf= min(mf, m[i])
    
    maxEle = 0
    for i in m:
        if(m[i] == mf):
            maxEle = max(maxEle, i)
    return maxEle


#{ 
 # Driver Code Starts
#Initial Template for Python 3

t = int(input())
#Iterating over test cases
for _ in range(t):
    n = int(input())
    arr = [int(x) for x in input().split()]
    print(LargButMinFreq(arr, n))
# } Driver Code Ends

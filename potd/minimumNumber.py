#User function Template for python3
# https://practice.geeksforgeeks.org/problems/7d62c8606123a199720c9b6885249dc9ac651bb7/1
class Solution:
    def minimumNumber(self, n, arr):
        m = min(arr)
        arr.pop(arr.index(m))
        for i in range(n-1):
            arr[i] = arr[i]%m
            if(arr[i] != 0):
                m = min(m,arr[i])
        for i in range(n-1):
            arr[i] = arr[i]%m
            if(arr[i] != 0):
                m = min(m,arr[i])
            # print(m,arr)
        return max(arr + [m])


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__=="__main__":
    for _ in range(int(input())):
        n=int(input())
        arr=[int(i) for i in input().split()]
        obj=Solution()
        print(obj.minimumNumber(n,arr))
# } Driver Code Ends

# link: https://practice.geeksforgeeks.org/problems/count-pairs-with-given-sum5022/1

#User function Template for python3

class Solution:
    def getPairsCount(self, arr, n, k):
        # # base case
        # if(n == 1):
        #     if(k == arr[0]):
        #         return 1
        #     else:
        #         return 0
                
        #general case
        m = {}
        ans = 0
        for i in range(n):
            try:
                m[arr[i]] += 1
            except:
                m[arr[i]] = 1
                
        for i in range(n):
            m[arr[i]] -= 1
            j = k - arr[i]
            try:
                ans += m[j]
            except:
                continue
            
        return ans


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    tc = int(input())
    while tc > 0:
        n, k = list(map(int, input().strip().split()))
        arr = list(map(int, input().strip().split()))
        ob = Solution()
        ans = ob.getPairsCount(arr, n, k)
        print(ans)
        tc -= 1

# } Driver Code Ends



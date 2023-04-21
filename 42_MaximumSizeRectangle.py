
# link: https://practice.geeksforgeeks.org/problems/max-rectangle/1
class Solution:
    def maxArea(self,M, n, m):
        # code here
        if not n or not m:
            return 0
            
        dp = [[0] * m for _ in range(n)]

        for i in range(n): # fill dp, value = number of 1s on the left side
            acc = 0
            
            for j in range(m):
                if M[i][j] == 1:
                    acc += 1
                else:
                    acc = 0
                    
                dp[i][j] = acc
                
        res = 0
        for i in reversed(range(n)):
            for j in reversed(range(m)):
                bSide, rSide = dp[i][j], 0 # bottom and right side
                k = i
         
                while k > -1 and dp[k][j]:  # iterate all possible rectangles
                    bSide = min(bSide, dp[k][j])
                    rSide += 1
                    res = max(res, bSide * rSide)
                    
                    k -= 1
                
        return res

#{ 
 # Driver Code Starts
#Initial Template for Python 3



# Driver Code 
if __name__ == '__main__':
    t=int(input())
    for _ in range(t):
        R,C = map(int, input().strip().split())
        A = []
        for i in range(R):
            line = [int(x) for x in input().strip().split()]
            A.append(line)
        print(Solution().maxArea(A, R, C)) 
	
# This code is contributed 
# by SHUBHAMSINGH10 

# } Driver Code Ends
'''
https://practice.geeksforgeeks.org/problems/express-as-sum-of-power-of-natural-numbers5647/1
'''
class Solution:
    def numOfWays(self, n, x):
        l = []
        mod = 10 ** 9 + 7
    
        for i in range(1, n + 1):
            curr = pow(i, x)
            if curr > n: break
            l.append(curr)
    
        dp = [[0 for _ in range(n + 1)] for _ in range(n + 1)]
    
        
        for i in range(n + 1):
            dp[i][0] = 1
    
 
        for i in range(len(l) - 1, -1, -1):
            for j in range(n, -1, -1):
                if j - l[i] >= 0:
                    dp[i][j] = (dp[i + 1][j - l[i]] + dp[i + 1][j]) % mod
                else:
                    dp[i][j] = dp[i + 1][j]
    
        return dp[0][n]


#{ 
 # Driver Code Starts
#Initial Template for Python 3
if __name__ == '__main__':
	T=int(input())
	for i in range(T):
		n,x = input().split()
		n=int(n)
		x=int(x)
		ob = Solution();
		print(ob.numOfWays(n, x))

# } Driver Code Ends

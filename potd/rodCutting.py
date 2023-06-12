'''
https://practice.geeksforgeeks.org/problems/rod-cutting0840/1
'''

class Solution:
    def cutRod(self, price, n):
        dp = [0]*(n+1)
        
        for i in range(1, n+1):
            max_val = -1
            for j in range(i):
                max_val = max(max_val, price[j] + dp[i-j-1])
            dp[i] = max_val
        
        return dp[n]


# class Solution:
#     def cutRod(self, price, n):
#         def cut_rod_helper(length:int) -> int:
#             if length == 0:
#                 return 0
            
#             max_val = -1
#             for i in range(length):
#                 max_val = max(max_val, price[i] + cut_rod_helper(length-i-1))
                
#             return max_val
        
#         return cut_rod_helper(n)


        


#{ 
 # Driver Code Starts
#Initial Template for Python 3

def main():

    T = int(input())

    while(T > 0):
        n = int(input())
        a = [int(x) for x in input().strip().split()]
        ob = Solution()
        print(ob.cutRod(a, n))

        T -= 1


if __name__ == "__main__":
    main()
# } Driver Code Ends

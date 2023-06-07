'''
https://practice.geeksforgeeks.org/problems/least-prime-factor5216/1
'''


import math
class Solution:
    
    def get_prime(self,k):
        if k%2==0:
            return 2
        
        else:
            for i in range(3,int(math.sqrt(k))+1,2):
                if k%i==0:
                    return i
        return k
    def leastPrimeFactor (self, n):
        # code here 
        l=[0,1]
        for i in range(2,n+1):
            l.append(self.get_prime(i))
        #print(l)
        return l


#{ 
 # Driver Code Starts
#Initial Template for Python 3
if __name__ == '__main__':
	T=int(input())
	for i in range(T):
		n = int(input())
		ob = Solution();
		ans = ob.leastPrimeFactor(n)
		for i in range(1, n+1):
			print(ans[i], end = " ")
		print()

# } Driver Code Ends

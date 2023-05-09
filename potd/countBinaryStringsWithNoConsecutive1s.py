'''
https://practice.geeksforgeeks.org/problems/37f36b318a7d99c81f17f0a54fc46b5ce06bbe8c/1
'''
class Solution:
    def countStrings(self, N):
        """
        Returns the count of all binary strings of length N without consecutive 1s.

        Args:
        N (int): The length of the binary strings.

        Returns:
        int: The count of all binary strings of length N without consecutive 1s.
        """
        # initialize M to 10^9 + 7
        M = 10**9+7
        
        # helper function for matrix multiplication
        def matrix_multiply(a, b):
            """
            Performs matrix multiplication on two matrices a and b.

            Args:
            a (list[list[int]]): The first matrix to multiply.
            b (list[list[int]]): The second matrix to multiply.

            Returns:
            list[list[int]]: The resulting matrix after multiplication.
            """
            nonlocal M
            # initialize a matrix with all elements set to 0
            c = [[0, 0], [0, 0]]
            # iterate over the rows and columns of the matrices and update the corresponding element in c
            for i in range(2):
                for j in range(2):
                    for k in range(2):
                        c[i][j] = (c[i][j]+a[i][k]*b[k][j])%M
            # return the resulting matrix c
            return c
        
        # helper function for matrix exponentiation
        def matrix_power(a, n):
            """
            Calculates the power of a matrix a raised to the power n.

            Args:
            a (list[list[int]]): The matrix to raise to the power n.
            n (int): The power to which the matrix is to be raised.

            Returns:
            list[list[int]]: The resulting matrix after exponentiation.
            """
            nonlocal M
            # initialize a matrix with all elements set to 1
            ans = [[1, 0], [0, 1]]
            # perform matrix multiplication iteratively
            while n > 0:
                if n%2 == 1:
                    ans = matrix_multiply(ans, a)
                a = matrix_multiply(a, a)
                n //= 2
            # return the resulting matrix ans
            return ans
        
        # call matrix_power with the matrix [[1, 1], [1, 0]] raised to the power N+1
        # return the value in the first row and first column of the resulting matrix
        return matrix_power([[1, 1], [1, 0]], N+1)[0][0]

# driver's code
if __name__ == '__main__':
    T = int(input())
    while T > 0: 
        ob = Solution()
        print(ob.countStrings(int(input())))
        T -= 1


'''
my failed attempt

class Solution:
    def __int__(self):
        self.cnt = 0
    def nextValidStr(self, s:str, i:int):
        print(cnt)
        print(s)
        if(i == len(s)):
            break
        nextValidStr(s[:i] + '0' + s[i+1:], i+1)
        nextValidStr(s[:i] + '1' + s[i+1:], i+1)
        return
    def countStrings(self, N): 
        self.nextValidStr("0"*N, 0)
        return cnt


#{ 
 # Driver Code Starts
#Initial Template for Python 3
#Initial Template for Python 3

if __name__ == '__main__':
    
    T = int(input())
    while T > 0: 
        
        ob = Solution()
        print(ob.countStrings(int(input())))
        
        T -= 1
# } Driver Code Ends
'''
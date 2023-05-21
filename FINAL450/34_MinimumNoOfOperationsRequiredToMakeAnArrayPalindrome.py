
# link: https://practice.geeksforgeeks.org/problems/palindromic-array/0

# Your task is to complete this function
# Function should return True/False or 1/0
def PalinArray(A, N):
    '''
    This function takes in an array A and its size N, and returns 1 if all elements of A are palindromes, or 0 otherwise.

    The function first iterates over all elements of A, and checks if each element is a palindrome by comparing its string representation with the reverse of its string representation. If any element is not a palindrome, the function immediately returns 0.

    If the loop completes without returning, it means that all elements of A are palindromes, and the function returns 1.
    '''
    # Iterate through the array and check if each element is a palindrome
    for i in range(N):
        if str(A[i]) != str(A[i])[::-1]:
            return 0

    # If all elements are palindromes, return 1
    return 1




#{ 
 # Driver Code Starts
# Driver Program
if __name__=='__main__':
    t=int(input())
    for i in range(t):
        n = int(input())
        arr = list(map(int, input().strip().split()))
        if PalinArray(arr, n):
            print(1)
        else:
            print(0)
# Contributed By: Harshit Sidhwa

# } Driver Code Ends



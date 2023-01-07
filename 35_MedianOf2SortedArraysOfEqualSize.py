
# link: https://practice.geeksforgeeks.org/problems/find-the-median0527/1

# User function Template for python3

class Solution:
    def find_median(self, arr):
        '''
        This function first sorts the array in ascending order. It then checks whether the length of the array is odd or even. If it is odd, it returns the middle element. If it is even, it returns the average of the two middle elements.
        '''
        # sort the array
        arr.sort()
        # if the length of the array is odd, return the middle element
        if len(arr) % 2 == 1:
            return arr[len(arr) // 2]
        # if the length of the array is even, return the average of the two middle elements
        else:
            return (arr[len(arr) // 2] + arr[len(arr) // 2 - 1]) // 2


# {
 # Driver Code Starts
# Initial Template for Python 3

if __name__ == '__main__':
    T = int(input())
    for i in range(T):
        n = int(input())
        v = list(map(int, input().split()))
        ob = Solution()
        ans = ob.find_median(v)
        print(ans)
# } Driver Code Ends

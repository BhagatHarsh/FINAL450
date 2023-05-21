
# link: https://practice.geeksforgeeks.org/problems/minimum-swaps-required-to-bring-all-elements-less-than-or-equal-to-k-together/0

#User function Template for python3

class Solution:
        
    def minSwap(self, arr, n, k):
        '''
        The first step in this code is to count the number of elements in the array arr that are less than or equal to k. This is done using a loop that iterates over all elements of arr, and a counter count that is incremented for each element that satisfies this condition.

        Next, the code initializes a counter count_legal_elements to 0, and then uses another loop to iterate over the first count elements of arr. For each element that is less than or equal to k, the counter count_legal_elements is incremented.

        After this, the code initializes a variable maxm to count_legal_elements. This will be used to keep track of the maximum number of elements less than or equal to k in any contiguous subarray of arr.

        The code then enters a loop that iterates over the remaining elements of arr. For each element, it first updates maxm to be the maximum of maxm and count_legal_elements. Then, it checks if the current element is less than or equal to k, and increments count_legal_elements if this is the case. Finally, it checks if the element at index j - count is less than or equal to k, and decrements count_legal_elements if this is the case.

        After the loop has completed, the code updates maxm to be the maximum of maxm and count_legal_elements. Finally, it calculates the minimum number of swaps required to bring all elements less than or equal to k together, which is equal to count - maxm, and returns this value.
        '''
        # Count the number of elements less than or equal to k
        count = 0
        for i in range(n):
            if arr[i] <= k:
                count += 1
    
        # Initialize the counter for the number of elements less than or equal to k
        count_legal_elements = 0
        for i in range(count):
            if arr[i] <= k:
                count_legal_elements += 1
    
        # Keep track of the maximum number of elements less than or equal to k
        maxm = count_legal_elements
        for j in range(count, n):
            # Update the maximum number of elements less than or equal to k
            maxm = max(maxm, count_legal_elements)
            # Check if the current element is less than or equal to k and update the counter
            if arr[j] <= k:
                count_legal_elements += 1
            # Check if the element at index j - count is less than or equal to k and update the counter
            if arr[j - count] <= k:
                count_legal_elements -= 1
    
        # Update the maximum number of elements less than or equal to k
        maxm = max(maxm, count_legal_elements)
        # Calculate the minimum number of swaps
        min_swaps = count - maxm
        return min_swaps






    




#{ 
 # Driver Code Starts
#Initial Template for Python 3

for _ in range(0,int(input())):
    n = int(input())
    arr = list(map(int, input().strip().split()))
    k = int(input())
    ob=Solution()
    ans = ob.minSwap(arr, n, k)
    print(ans)
    





# } Driver Code Ends



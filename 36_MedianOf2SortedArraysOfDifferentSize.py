# link: https://www.geeksforgeeks.org/median-of-two-sorted-arrays-of-different-sizes/


class Solution:

    # Method to find median
    def Median(self, A, B):

        # Assumption both A and B cannot be empty
        n = len(A)
        m = len(B)
        if (n > m):
            return self.Median(B, A)  # Swapping to make A smaller

        start = 0
        end = n
        realmidinmergedarray = (n + m + 1) // 2

        while (start <= end):
            mid = (start + end) // 2
            leftAsize = mid
            leftBsize = realmidinmergedarray - mid

            # checking overflow of indices
            leftA = A[leftAsize - 1] if (leftAsize > 0) else float('-inf')
            leftB = B[leftBsize - 1] if (leftBsize > 0) else float('-inf')
            rightA = A[leftAsize] if (leftAsize < n) else float('inf')
            rightB = B[leftBsize] if (leftBsize < m) else float('inf')

            # if correct partition is done
            if leftA <= rightB and leftB <= rightA:
                if ((m + n) % 2 == 0):
                    return (max(leftA, leftB) + min(rightA, rightB)) / 2.0
                return max(leftA, leftB)

            elif (leftA > rightB):
                end = mid - 1
            else:
                start = mid + 1


# Driver code
ans = Solution()
arr1 = [-5, 3, 6, 12, 15]
arr2 = [-12, -10, -6, -3, 4, 10]
print("Median of the two arrays is")
print(ans.Median(arr1, arr2))

# This code is contributed by Arpan
'''
Exaplaination
Here are the steps the code takes to calculate the median of two sorted arrays:

First, it declares a class named "Solution" which contains a method called "Median" that takes two sorted arrays, A and B as its input.

Next, it initializes two variables "n" and "m" to the length of array A and array B respectively. Then, it checks if the length of A is greater than that of B. If it is, it swaps the input arrays such that A is always smaller than B.

The method then sets the initial values for start and end, which are used to define a range for binary search. And it also set real median of merged array

The method then enters a while loop that continues until the value of "start" is less than or equal to "end". Inside the loop, it first calculates the middle point (mid) of the current range using integer division.

It then calculates the size of the left part of array A and left part of array B based on the value of "mid".

Next, it checks for overflow of indices by checking if "leftAsize" and "leftBsize" are greater than 0. If they are, it assigns the value of the element at that index in A and B to "leftA" and "leftB" respectively. Otherwise, it assigns the value of negative infinity to "leftA" and "leftB". Similarly, it does for rightA and rightB.

The method then checks if the correct partition of the arrays has been done. It checks if "leftA" is less than or equal to "rightB" and "leftB" is less than or equal to "rightA". If this is the case, the method checks if the total number of elements in the merged array is even. If it is, it calculates the median as the average of the maximum of "leftA" and "leftB" and the minimum of "rightA" and "rightB", and returns this value. If the total number of elements is odd, it returns the maximum of "leftA" and "leftB" as the median.

If the correct partition has not been done, it checks if "leftA" is greater than "rightB". If it is, it decrements the value of "end" by 1 and continues the loop. Otherwise, it increments the value of "start" by 1 and continues the loop.

Finally, the median of the two arrays is returned.

It's important to note that for this code to work correctly both arrays need to be sorted and it will give the median of the merged sorted array.

'''

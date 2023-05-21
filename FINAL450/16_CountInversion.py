
#link: https://practice.geeksforgeeks.org/problems/inversion-of-array/0

'''
count the number of times a number is smaller then its prefix elements

TLE approach:
long long int inversionCount(long long arr[], long long N)
{
    long long int val = 0;
    for(long long int i=0;i<N;++i){
        for(long long int j=i+1;j<N;++j)
        if(arr[i]>arr[j])
        ++val;
    }
    return val;
}

valid approach:

'''


class Solution:
    #User function Template for python3
    
    # arr[]: Input Array
    # N : Size of the Array arr[]
    #Function to count inversions in the array.
    
    
    def inversionCount(self, arr, n):
        result = self.merge_sort(arr,0,n-1)
        return result

    def merge_sort(self,arr,left,right):
        result = 0
        if(left<right):
            mid = (left+right)//2
            result+= self.merge_sort(arr,left,mid)
            result+=self.merge_sort(arr,mid+1,right)
            result+=self.merge(arr,left,mid,right)
        return result

    def merge(self,arr,left,mid,right):
        l = arr[left:mid+1]
        r = arr[mid+1:right+1]
        i = 0;j=0;k=left;count = 0
        n1 = len(l);n2 = len(r)
        while(i<len(l) and j<len(r)):
            if(l[i]<=r[j]):
                arr[k] = l[i]
                k+=1
                i+=1

            else:
                arr[k] = r[j]
                j+=1
                k+=1
                count += n1-i

        while(i<n1):
            arr[k]=l[i]
            i+=1
            k+=1

        while(j<n2):
            arr[k]=r[j]
            j+=1
            k+=1

        return count


#{ 
 # Driver Code Starts
#Initial Template for Python 3

import atexit
import io
import sys


_INPUT_LINES = sys.stdin.read().splitlines()
input = iter(_INPUT_LINES).__next__
_OUTPUT_BUFFER = io.StringIO()
sys.stdout = _OUTPUT_BUFFER

@atexit.register

def write():
    sys.__stdout__.write(_OUTPUT_BUFFER.getvalue())

if __name__=='__main__':
    t = int(input())
    for tt in range(t):
        n = int(input())
        a = list(map(int, input().strip().split()))
        obj = Solution()
        print(obj.inversionCount(a,n))
# } Driver Code Ends
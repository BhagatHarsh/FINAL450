//{ Driver Code Starts
#include <bits/stdc++.h>
using namespace std;

// } Driver Code Ends
class Solution
{
public:
    // arr: input array
    // n: size of array
    // Function to find the sum of contiguous subarray with maximum sum.
    /*
    This was a bit embarssing when you actually try and think it through
    it gets really complex while the alogrithm is really simple
    */
    long long maxSubarraySum(int a[], int n)
    {

        long long sum = 0, maxSum = INT_MIN;
        long long i, j, k, neg = 0, pos = 0;
        for (i = 0; i < n; ++i)
        {

            sum += a[i];
            maxSum = max(maxSum, sum);
            sum = max((long long)0, sum);
        }

        return maxSum;
    }
};

//{ Driver Code Starts.

int main()
{
    int t, n;

    cin >> t;   // input testcases
    while (t--) // while testcases exist
    {

        cin >> n; // input size of array

        int a[n];

        for (int i = 0; i < n; i++)
            cin >> a[i]; // inputting elements of array

        Solution ob;

        cout << ob.maxSubarraySum(a, n) << endl;
    }
}

// } Driver Code Ends
//{ Driver Code Starts
#include <bits/stdc++.h>
using namespace std;

// } Driver Code Ends
// Function to return minimum number of jumps to end of array

class Solution
{
public:
    int minJumps(int arr[], int n)
    {
        if (n == 1)
            return 0;
        int countJp = 0;
        int i = 0;
        while (arr[i] + i < n - 1)
        {
            if (arr[i] == 0)
                return -1;
            if (arr[i] == 1)
            {
                countJp++;
                i++;
            }
            else
            {
                int maxJump = 0;
                int k = 1;
                int jumpIdx;
                while (k <= arr[i])
                {
                    if (maxJump < (arr[i + k] + i + k))
                    {
                        maxJump = arr[i + k] + i + k;
                        jumpIdx = i + k;
                    }
                    k++;
                }
                i = jumpIdx;
                countJp++;
            }
        }
        return countJp + 1;
    }
};

//{ Driver Code Starts.

int main()
{
    int t;
    cin >> t;
    while (t--)
    {
        int n, i, j;
        cin >> n;
        int arr[n];
        for (int i = 0; i < n; i++)
            cin >> arr[i];
        Solution obj;
        cout << obj.minJumps(arr, n) << endl;
    }
    return 0;
}

// } Driver Code Ends
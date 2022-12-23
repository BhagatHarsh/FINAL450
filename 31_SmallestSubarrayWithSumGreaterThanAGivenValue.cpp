
//link: https://practice.geeksforgeeks.org/problems/smallest-subarray-with-sum-greater-than-x/0

//{ Driver Code Starts
#include <bits/stdc++.h>
using namespace std;


// } Driver Code Ends
class Solution{
  public:
    /*
    Check add the numbers till the sum gooes above.
    subtract till the sum goes down and find the minimum length.
    */
    int smallestSubWithSum(int arr[], int n, int x)
    {
        int sum = 0, i = 0, j = 0, len = INT_MAX;
        while(i < n) {
            sum += arr[i];
            if(sum > x) {
                while(sum > x) {
                    len = min(len,i - j + 1);
                    sum -= arr[j];
                    j++;
                }
            }
            i++;
        }
        return len;
    }
};

//{ Driver Code Starts.

int main() {
	// your code goes here
	int t;
	cin>>t;
	while(t--)
	{
		int n,x;
		cin>>n>>x;
		int a[n];
		for(int i=0;i<n;i++)
		cin>>a[i];
		Solution obj;
		cout<<obj.smallestSubWithSum(a,n,x)<<endl;
	}
	return 0;
}
// } Driver Code Ends



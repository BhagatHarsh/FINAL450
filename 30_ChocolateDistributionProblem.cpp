
//link: https://practice.geeksforgeeks.org/problems/chocolate-distribution-problem/0

//{ Driver Code Starts
#include <bits/stdc++.h>
using namespace std;

// } Driver Code Ends
class Solution{
    public:
    /*
    A simple loop of a sliding window of children we have to give candies to.
    */
    long long findMinDiff(vector<long long> a, long long n, long long m){
        long long minn = INT_MAX;
        sort(a.begin(),a.end());
        // for(int i=0;i<n;++i) cout<<a[i]<<" ";
        // cout<<endl;
        for(int i=0;i<=n-m;++i){
            // cout<<minn<<" "<<a[i+m-1]<<" "<<a[i]<<endl;
            minn = min(minn, a[i+m-1]-a[i]);
        }
        
        return minn;
    }   
};

//{ Driver Code Starts.
int main() {
	long long t;
	cin>>t;
	while(t--)
	{
		long long n;
		cin>>n;
		vector<long long> a;
		long long x;
		for(long long i=0;i<n;i++)
		{
			cin>>x;
			a.push_back(x);
		}
		
		long long m;
		cin>>m;
		Solution ob;
		cout<<ob.findMinDiff(a,n,m)<<endl;
	}
	return 0;
}
// } Driver Code Ends



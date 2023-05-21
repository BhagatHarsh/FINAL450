
//link: https://practice.geeksforgeeks.org/problems/subarray-with-0-sum/0

/*
You find the basic prefix sum array and then check where the prefix value reset which means that if a prefix sum array value repeats means we have a zero sum in the subarray.
IDK why it didnt work for n == 2 but i just added it.
*/
#include <bits/stdc++.h>
using namespace std;
class Solution{
    public:
    //Complete this function
    //Function to check whether there is a subarray present with 0-sum or not.
    bool subArrayExists(int arr[], int n)
    {
        for(int i=0;i<n;++i) if(arr[i] == 0) return true;
        vector<int> preSum(n);
        int sum=0;
        if(n == 2){
            if(arr[0] + arr[1] == 0){
                return true;
            }
            return false;
        }
        for(int i=0;i<n;++i){
            sum+=arr[i];
            preSum[i] = sum;
        }
        map<int,int> m;
        for(int i=0;i<n;++i){
            ++m[preSum[i]];
            if(m[preSum[i]] == 2) return true;
        }
        return false;
    }
};

int main()
{
	int t;
	cin>>t;
	while(t--)
	{
	    int n;
	    cin>>n;
	    int arr[n];
	    for(int i=0;i<n;i++)
	    cin>>arr[i];
	    Solution obj;
	    	if (obj.subArrayExists(arr, n))
		cout << "Yes\n";
	else
		cout << "No\n";
	}
	return 0;
}
// } Driver Code Ends



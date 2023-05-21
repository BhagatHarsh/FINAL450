
//link: https://practice.geeksforgeeks.org/problems/triplet-sum-in-array/0

//{ Driver Code Starts
#include <bits/stdc++.h>
using namespace std;
/*
The trick here is to use binary search as we know that the sum is X.
we choose a pivot and then try binary search across the sum.
changing l and r accordingly.
*/

// } Driver Code Ends
class Solution{
    public:
    //Function to find if there exists a triplet in the 
    //array A[] which sums up to X.
    bool find3Numbers(int A[], int n, int X)
    {
        if(n<3){
            return false;
        }
        sort(A,A+n);
        int i,l,r,res;
        for(int i=0;i<n-2;i++){
            l=i+1;
            r=n-1;
            while(l<r){
            res=A[i]+A[l]+A[r]; //required number 
            if(res==X){
                return true;
            }else if(res>X){ // if bigger means we need smaller numbers to add up
                r=r-1;
            }else{
                l=l+1; //if lower then we need bigger numbers to add up
            }
        }
    }
        return false;
    }

};

//{ Driver Code Starts.

int main()
{
	int T;
	cin>>T;
	while(T--)
	{
		int n,X;
		cin>>n>>X;
		int i,A[n];
		for(i=0;i<n;i++)
			cin>>A[i];
		Solution ob;
        cout <<  ob.find3Numbers(A, n, X) << endl;
    }
}

// } Driver Code Ends




//link: https://practice.geeksforgeeks.org/problems/longest-consecutive-subsequence/0

//{ Driver Code Starts
#include <bits/stdc++.h>
using namespace std;

/*
Using counting sort
*/
class Solution{
  public:
    // arr[] : the input array
    // N : size of the array arr[]
    
    //Function to return length of longest subsequence of consecutive integers.
    int findLongestConseqSubseq(int arr[], int N)
    {
      //Your code here
      int mp[100001]={0} ;
      
      for(int i=0 ;i<N;i++)
      mp[arr[i]]++;
      
      int ans=0; 
      int maxi= 0;  
    
        int i=0 ;
        while(i<100001)
        {
            if(mp[i]>=1)
            {
                ans++;
                maxi= max(ans, maxi) ;
            }
            else 
                ans =0 ;
            i++;
        }
        return maxi ;
    }
};

//{ Driver Code Starts.
 
// Driver program
int main()
{
 int  t,n,i,a[100001];
 cin>>t;
 while(t--)
 {
  cin>>n;
  for(i=0;i<n;i++)
  cin>>a[i];
  Solution obj;
  cout<<obj.findLongestConseqSubseq(a, n)<<endl;
 }
      
    return 0;
}
// } Driver Code Ends



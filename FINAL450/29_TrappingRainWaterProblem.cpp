
//link: https://practice.geeksforgeeks.org/problems/trapping-rain-water/0

//{ Driver Code Starts
#include<bits/stdc++.h>

using namespace std;


// } Driver Code Ends
class Solution{

    // Function to find the trapped water between the blocks.
    public:
    /*
    Sometimes a problem may take a while to solve but when its done by you the reward is far more worth the pain.
    created a running lastMin which when refreshed adds up all the water by backtracking.
    */
    long long trappingWater(int arr[], int n){
        map<int , long long> drops;
        int lastMin = arr[0],rem = 0,lastInd=0;
        for(int i=0;i<n;++i){
            if(arr[i] >= lastMin){
                for(int j=i-1;j>=lastInd;--j){
                    drops[j]=lastMin-arr[j];
                }
                lastMin = arr[i];
                lastInd = i;
            }
        }
        
        
        
        lastMin = arr[n-1],rem = 0,lastInd=n-1;
        for(int i=n-1;i>=0;--i){
            if(arr[i]>=lastMin){
                for(int j=lastInd;j>i;--j){
                    drops[j] = lastMin - arr[j];
                }
                lastMin = arr[i];
                lastInd = i;
            }
        }
        long long ans = 0;
        for(auto i:drops){
            // cout<<i.first<<" "<<i.second<<endl;
            ans += i.second;
        }
        
        return ans;
    }
};

//{ Driver Code Starts.

int main(){
    
    int t;
    //testcases
    cin >> t;
    
    while(t--){
        int n;
        
        //size of array
        cin >> n;
        
        int a[n];
        
        //adding elements to the array
        for(int i =0;i<n;i++){
            cin >> a[i];            
        }
        Solution obj;
        //calling trappingWater() function
        cout << obj.trappingWater(a, n) << endl;
        
    }
    
    return 0;
}
// } Driver Code Ends



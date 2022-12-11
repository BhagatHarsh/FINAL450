
//link: https://practice.geeksforgeeks.org/problems/array-subset-of-another-array/0

//{ Driver Code Starts
#include <bits/stdc++.h>
using namespace std;

/*
Creating a map of elements of a1 and then subtracting them with a2
if an element is not found then it is reported.
*/

string isSubset(int a1[], int a2[], int n, int m) ;

int main() {
    int t;
    cin >> t;

    while (t--) {
        int n, m;
        cin >> n >> m;
        int a1[n], a2[m];

        for (int i = 0; i < n; i++) {
            cin >> a1[i];
        }
        for (int i = 0; i < m; i++) {
            cin >> a2[i];
        }

        cout << isSubset(a1, a2, n, m) << endl;
    }
    return 0;
}

// } Driver Code Ends


string isSubset(int a1[], int a2[], int n, int m) {
    map<int,int> mp;
    for(int i=0;i<n;++i){
        ++mp[a1[i]];
    }
    int flag = 1;
    for(int i=0;i<m;++i){
        if(mp[a2[i]] == 0){
            flag = 0;break;
        }
        --mp[a2[i]];
    }
    
    if(flag) return "Yes"; else return "No";
}



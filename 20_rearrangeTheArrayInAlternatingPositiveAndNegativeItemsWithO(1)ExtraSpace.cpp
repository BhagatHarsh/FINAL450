
//link: https://www.geeksforgeeks.org/rearrange-array-alternating-positive-negative-items-o1-extra-space/
/*
Rearrange array in alternating positive & negative items with O(1) extra space 
*/

#include <bits/stdc++.h>
using namespace std;
#define ll long long int
#define endl '\n'

int main(){
    ll t,n;
    cin>>t;
    while(t--){
        cin>>n;
        vector<int> v(n);
        int neg = 0;
        for(int i=0;i<n;++i) {
            cin>>v[i];
            ++neg;
        }
            for(int i=0;i<n && neg; ++i){
                if(i%2 == 0 && i >= 0){
                    for(int j=i+1;j<n;++j){
                        if(v[j]<0){
                            swap(v[i],v[j]);
                            --neg;
                            break;
                        }
                    }
                }
            }
            for(int i=0;i<n;++i){
                cout<<v[i]<<" ";
            }cout<<endl;
    }
    return 0;
}



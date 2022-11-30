//Link : 
/* Notes :
This problem looks like the merge sort opetion which we use to finally combine the two arrays.
*/
#include<bits/stdc++.h>
using namespace std;

int main(){
#define int long long int
ios_base::sync_with_stdio(false); cin.tie(NULL);
int t,n;
cin>>t;
while(t--){
    cin>>n;
    int a[n],b[n],c[2*n];
    for(int i=0;i<n;i++) cin>>a[i];
    for(int i=0;i<n;i++) cin>>b[i];
    int i=0,j=0,k=0;
    while(i<n && j<n){
        if(a[i]<b[j]){
            c[k++] = a[i];
            i++;
        }
        else{
            c[k++] = b[j];
            j++;
        }
    }
    while(i<n){
        c[k++] = a[i];
        i++;
    }
    while(j<n){
        c[k++] = b[j];
        j++;
    }
    for(int i=0;i<2*n;i++) cout<<c[i]<<" ";
    cout<<endl;
}
return 0;
}
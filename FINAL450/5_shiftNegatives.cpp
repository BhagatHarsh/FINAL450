// Link : https://www.geeksforgeeks.org/move-negative-numbers-beginning-positive-end-constant-extra-space/
/* Notes :

the two pointer method looks good enough and has similar time complexity as the other methods
*/
#include <bits/stdc++.h>
using namespace std;

int main()
{
#define int long long int
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    int n, x;
    cin >> n;
    vector<int> v(n);
    for (int i = 0; i < n; i++)
    {
        cin >> v[i];
    }
    int i = 0, j = 0;
    while (j < n)
    {
        if (v[j] < 0)
        {
            swap(v[i], v[j]);
            i++;
        }
        j++;
    }
    for (int i = 0; i < n; i++)
    {
        cout << v[i] << " ";
    }
    return 0;
}
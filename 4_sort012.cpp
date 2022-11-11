//{ Driver Code Starts
#include <bits/stdc++.h>
using namespace std;

// Implemented a map apporach

// } Driver Code Ends
class Solution
{
public:
    void sort012(int a[], int n)
    {
        map<int, int> m;
        for (int i = 0; i < n; ++i)
        {
            ++m[a[i]];
        }
        int j = 0;
        for (int i = 0; i < m[0]; ++i, ++j)
            a[j] = 0;
        for (int i = 0; i < m[1]; ++i, ++j)
            a[j] = 1;
        for (int i = 0; i < m[2]; ++i, ++j)
            a[j] = 2;
    }
};

//{ Driver Code Starts.
int main()
{

    int t;
    cin >> t;

    while (t--)
    {
        int n;
        cin >> n;
        int a[n];
        for (int i = 0; i < n; i++)
        {
            cin >> a[i];
        }

        Solution ob;
        ob.sort012(a, n);

        for (int i = 0; i < n; i++)
        {
            cout << a[i] << " ";
        }

        cout << endl;
    }
    return 0;
}

// } Driver Code Ends
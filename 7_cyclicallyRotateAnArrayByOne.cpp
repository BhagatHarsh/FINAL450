//{ Driver Code Starts
// Initial Template for C++

#include <bits/stdc++.h>
using namespace std;
void rotate(int arr[], int n);

int main()
{
    int t;
    scanf("%d", &t);
    while (t--)
    {
        int n;
        scanf("%d", &n);
        int a[n], i;
        for (i = 0; i < n; i++)
            scanf("%d", &a[i]);
        rotate(a, n);
        for (i = 0; i < n; i++)
            printf("%d ", a[i]);
        printf("\n");
    }
    return 0;
}

// } Driver Code Ends

// User function Template for C++

/*
Had to think it through for a while to get the logic right
but it was just simple swapping of elements
*/

* /

    void rotate(int a[], int n)
{
    if (n == 1)
        return;
    int temp = a[n - 1], tmp;
    for (int i = n - 1; i > 0; --i)
    {
        tmp = a[i - 1];
        a[i - 1] = a[i];
        a[i] = tmp;
    }
    a[0] = temp;
}
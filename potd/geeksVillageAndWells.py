'''
TLE in testcase 1116

code:
#User function Template for python3
from typing import List
from collections import deque

class Solution:
    def chefAndWells(self, n: int, m: int, c: List[List[str]]) -> List[List[int]]:
        ans = [[-1] * m for _ in range(n)]
        q = deque()
        
        # Initialize the queue and set values in ans
        for i in range(n):
            for j in range(m):
                if c[i][j] == 'N' or c[i][j] == 'W':
                    ans[i][j] = 0
                if c[i][j] == 'W':
                    q.append((i, j, 0))
        
        # Define the four possible directions of movement
        dir = [(0, -1), (0, 1), (-1, 0), (1, 0)]
        
        # Multi-source BFS
        while q:
            i, j, currSteps = q.popleft()
            for dx, dy in dir:
                newI, newJ = i + dx, j + dy
                if newI < 0 or newI >= n or newJ < 0 or newJ >= m or ans[newI][newJ] != -1:
                    continue
                if c[newI][newJ] == 'W' or c[newI][newJ] == 'N':
                    continue
                q.append((newI, newJ, currSteps + 1))
                ans[newI][newJ] = currSteps + 1
        
        # Post-processing
        for i in range(n):
            for j in range(m):
                if ans[i][j] != -1:
                    ans[i][j] *= 2
                if c[i][j] == '.':
                    ans[i][j] = 0
        
        return ans
'''
'''
CPP solution from the comments same approach

code:
//{ Driver Code Starts
//Initial Template for C++

#include <bits/stdc++.h>
using namespace std;


// } Driver Code Ends
//User function Template for C++
class Solution{
    public:
  vector<vector<int>> chefAndWells(int n,int m,vector<vector<char>> &arr){
        vector<vector<int>> ans(n,vector<int>(m,-1));
        queue<pair<pair<int,int>,int>> q;
        
        for(int i=0;i<n;i++){
            for(int j=0;j<m;j++){
                if(arr[i][j] == 'N' || arr[i][j] == 'W'){
                    ans[i][j] = 0;
                }
                if(arr[i][j] == 'W'){
                    q.push({{i,j},0});
                }
            }
        }
        
        vector<pair<int,int>> dir = {{0,-1},{0,1},{-1,0},{1,0}};
        
        while(q.size() != 0){
            pair<pair<int,int>,int> front = q.front();
            q.pop();
            
            int i = front.first.first;
            int j = front.first.second;
            int currSteps = front.second;
            
            for(auto it:dir){
                int newI = i + it.first;
                int newJ = j + it.second;
                
                if(newI < 0 || newI >= n || newJ < 0 || newJ >= m || ans[newI][newJ] != -1){
                    continue;
                }
                
                if(arr[newI][newJ] == 'W' || arr[newI][newJ] == 'N'){
                    continue;
                }
                
                q.push({{newI,newJ},currSteps+1});
                ans[newI][newJ] = currSteps+1;
            }
        }
        
        // Because they have to return as well to there home
        for(int i=0;i<n;i++){
            for(int j=0;j<m;j++){
                if(ans[i][j] != -1){
                    ans[i][j] *= 2;
                }
                // Because grounds does not need water but they must be in path.
                if(arr[i][j] == '.'){
                    ans[i][j] = 0;
                }
            }
        }
        
        return ans;
    }  
    
};

//{ Driver Code Starts.

int main(){
    int t;
    cin>>t;
    while(t--){
        int n,m;
        cin>>n>>m;
        vector<vector<char>> c(n,vector<char>(m));
        for(int i=0;i<n;i++){
            for(int j=0;j<m;j++){
                cin>>c[i][j];
            }
        }
        Solution ob;
        vector<vector<int>> res=ob.chefAndWells(n,m,c);
        for(int i=0;i<n;i++){
            for(int j=0;j<m;j++){
                cout<<res[i][j]<<" ";
            }
            cout<<endl;
        }
    }
}
// } Driver Code Ends
'''

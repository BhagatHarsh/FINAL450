'''
https://practice.geeksforgeeks.org/problems/c6ced401352fd126b89129cd562a9247f057e40e/1
'''

class Solution:
    def findMoves(self,n,chairs,passengers):
        ans = 0
        chairs.sort()
        passengers.sort()
        for i in range(n):
            ans += abs(chairs[i] - passengers[i])
        return ans

#{ 
 # Driver Code Starts.
if __name__=="__main__":
    for _ in range(int(input())):
        n=int(input())
        a=[int(i) for i in input().split()]
        b=[int(i) for i in input().split()]
        obj=Solution()
        print(obj.findMoves(n,a,b))
        
# } Driver Code Ends
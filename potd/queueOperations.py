'''
https://practice.geeksforgeeks.org/problems/queue-operations/1
'''

#User function Template for python3
class Solution:
    def __init__(self) -> None:
        self.mp = {}
        return
    # Function to insert element into the queue
    def insert(self, q, k) -> None: 
        try:
            self.mp[k]+=1
        except:
            self.mp[k] = 1
        return
        #code here
        
    # Function to find frequency of an element
    # return the frequency of k
    def findFrequency(self, q, k):
        try:
            return self.mp[k]
        except:
            return -1


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__': 
    t = int(input())
    for _ in range(t):
        obj = Solution()
        q = []
        n = int(input())
        arr = list(map(int, input().strip().split()));
        for k in arr:
            obj.insert(q,k)
        
        
        m = int(input())
        query = list(map(int, input().strip().split()));
        for k in query:
            f = obj.findFrequency(q,k)
            if f!=0:
                print(f)
            else:
                print(-1)

# } Driver Code Ends

'''
https://practice.geeksforgeeks.org/problems/hands-of-straights/1
'''

import heapq
class Solution:
    def isStraightHand(self, N, groupSize, hand):
        if(N%groupSize):
            return False

        m = {}
        
        for i in hand:
            try:
                m[i]+=1
            except:
                m[i]=1
        
        heap = list(m.keys())
        heapq.heapify(heap)
        while(heap):
            minEle = heap[0]
            for i in range(minEle, minEle + groupSize):
                if(i not in m):
                    return False
                m[i]-=1
                
                if(m[i] == 0):
                    if(i != heap[0]):
                        return False
                    heapq.heappop(heap)
                
        return True

#{ 
 # Driver Code Starts.
if __name__ == '__main__': 
    t = int(input ())
    for _ in range (t):
        N, groupSize = list(map(int, input().split()))
        hand = list(map(int, input().split()))
        ob = Solution()
        res = ob.isStraightHand(N, groupSize, hand);
        print(res)
# } Driver Code Ends
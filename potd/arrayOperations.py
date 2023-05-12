'''
https://practice.geeksforgeeks.org/problems/3a93b6a25a7b88e4c80a1fee00898fd8022eb108/1
'''
class Solution:
    def arrayOperations(self, n : int, arr : List[int]) -> int:
        ans = 0
        prev_num = 0
        num_zero = 0
        for i in arr:
            if i:       # i  != 0
                if not prev_num:    # prev_num == 0
                    num_zero += 1
            prev_num = i
        return num_zero

'''
My attempt

Question has wrong test cases
'''

from typing import List
import numpy as np

class Solution:
    def arrSplit(self, l: List[int], ii: int) -> List[List[int]]:
        n = len(l)
        i = 0
        ans = []
        tmp = []
        while(i<n):
            if(l[i] == ii):
                j = i+1
                if(len(tmp)):
                    ans.append(tmp)
                tmp = []
                while(j<n):
                    if(l[j] != ii):
                        tmp.append(l[j])
                    else:
                        break
                    j+=1
                i+=j-1
                if(len(tmp)):
                    ans.append(tmp)
                tmp = []
            else:
                tmp.append(l[i])
            i+=1
        if(len(tmp)):
            ans.append(tmp)
        if(len(ans)):
            return ans
        return []
    
    def arrayOperations(self, n : int, arr : List[int]) -> int:
        s = self.arrSplit(arr, 0)
        if(len(s) == 1):
            return -1
        return len(s)


#{ 
 # Driver Code Starts
class IntArray:
    def __init__(self) -> None:
        pass
    def Input(self,n):
        arr=[int(i) for i in input().strip().split()]#array input
        return arr
    def Print(self,arr):
        for i in arr:
            print(i,end=" ")
        print()


if __name__=="__main__":
    t = int(input())
    for _ in range(t):
        
        n = int(input())
        
        
        arr=IntArray().Input(n)
        
        obj = Solution()
        res = obj.arrayOperations(n, arr)
        
        print(res)
        

# } Driver Code Ends
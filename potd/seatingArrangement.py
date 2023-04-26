from typing import List

'''
WA testcase 18
'''
class Solution:
    def is_possible_to_get_seats(self, n : int, m : int, seats : List[int]) -> bool:
        if(n == 0):
            return True
        if(m == 1):
            if(n > 1):
                return False
            if(seats[0]):
                return False
            else:
                return True
        if(m == 2):
            if(n > 1):
                return False
            s = sum(seats)
            if(s == 0):
                return True
            else:
                return False
        for i in range(1,m-1):
            if(seats[i-1] == seats[i] and seats[i] == seats[i+1] and seats[i] == 0):
                n-=1
                seats[i] = 1
        if(seats[0] == 0 and seats[1] == 0 and seats[2] == 1):
            n-=1
            seats[0] =1
        if(seats[-1] == 0 and seats[-2] == 0 and seats[-3] == 1):
            n-=1
            seats[-1] = 1
        # print(seats)
        return n <= 0
        

'''
Solution from comments
'''

def is_possible_to_get_seats(self, n : int, m : int, seats : List[int]) -> bool:
        # code here
        available=1#CoverYourBase
        ans=0
        for i in range(m):
            if seats[i]==0:
                available+=1 
            else:
                ans+=max(0,(available-1)//2)
                available=0
        
        available+=1#ZeroDefence    
        ans+=(available-1)//2
                
        if ans>=n:
            return True
        else:
            return False
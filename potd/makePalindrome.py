'''
https://practice.geeksforgeeks.org/problems/8d0e8785cef59cf4903b926ceb7100bcd16a9835/1
my attempt 
Test Cases Passed: 
1011 /1120
Time Limit Exceeded
'''

from typing import List
from collections import Counter

class Solution:
    def makePalindrome(self, n : int, arr : List[str]) -> bool:
        l = []
        left = []
        right = []
        flag = True
        for i in range(n):
            for j in range(i+1,n):
                # print(arr[i],arr[j],arr[j][::-1],arr[i] is arr[j][::-1])
                flag = True
                if(arr[i] != "" and arr[i] == arr[j][::-1]):
                    left.append(arr[i])
                    right.append(arr[j])
                    arr[j] = ""
                    flag = False
                    break
            if(flag and arr[i] != ''):
                l.append(arr[i])
        m = len(l)
        if(m == 0):
            return True
        elif(m == 1):
            if(n%2 == 0):
                return False
            final = ''.join(left) + l[0] + ''.join(list(reversed(right)))
            if(final == final[::-1]):
                return True
            else:
                return False
        return False


'''
True solution from the commments
'''

def makePalindrome(self, n : int, arr : List[str]) -> bool:
    a=[]
    for i in arr: a.append(i[::-1])
    return sorted(a)==sorted(arr)
        

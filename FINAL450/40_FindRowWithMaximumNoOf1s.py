
# link: https://practice.geeksforgeeks.org/problems/row-with-max-1s0023/1

#User function Template for python3
class Solution:
    def rowWithMax1s(self,arr, n, m):
        # code here
        max1 = 0
        maxi = 0
        flag = 0
        for i in range(n):
          #  print(i,i.count(1))
          mox = arr[i].count(1)
          if(mox>max1):
              max1 = mox
              maxi = i
              flag = 1
        if(flag == 1):
            return maxi
        else:
            return -1



'''
https://practice.geeksforgeeks.org/problems/0a7c7f1089932257071f9fa076f25d353f91e0fd/1
'''


class Solution:

    def maxSweetness(self, sweetness, n, k):
        left = 1  # minimum possible sweetness value
        right = sum(sweetness)  # maximum possible sweetness value
        result = 0
        while left <= right:
            mid = (left + right) // 2
            if self.canDivide(sweetness, n, k, mid):
                result = mid
                left = mid + 1
            else:
                right = mid - 1
        return result

    # helper function to check if it is possible to divide the chocolate
    # into K + 1 pieces with minimum sweetness value at least as high as target
    def canDivide(self, sweetness, n, k, target):
        pieces = 0
        total = 0
        for i in range(n):
            total += sweetness[i]
            if total >= target:
                pieces += 1
                total = 0
        return pieces >= k + 1

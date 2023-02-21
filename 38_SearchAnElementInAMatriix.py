# link: https://leetcode.com/problems/search-a-2d-matrix/


class Solution:

    def searchMatrix(self, L: List[List[int]], t: int) -> bool:
        flag = 0
        for i in range(len(L)):
            if (L[i][0] <= t <= L[i][len(L[i]) - 1]):
                for j in L[i]:
                    print(j)
                    if (j == t):
                        return True
                    else:
                        flag = 1
            elif (flag == 1):
                break
        return False

'''
https://leetcode.com/problems/special-positions-in-a-binary-matrix/description/?envType=daily-question&envId=2023-12-13
'''

class Solution:
    def numSpecial(self, mat: List[List[int]]) -> int:
        n = len(mat)
        m = len(mat[0])

        special = 0
        for i in range(m):
            temp = 0
            ind = 0
            for j in range(n):
                temp += mat[j][i]
                if(mat[j][i]):
                    ind = j
            
            if(temp == 1):
                if(sum(mat[ind]) == 1):
                    special += 1

                
        return special
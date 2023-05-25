'''
https://practice.geeksforgeeks.org/problems/expression-add-operators/1
'''
class Solution:
    def dfs(self, index, s, target, ans, temp, prev, res):
        # base case
        if index == len(s):
            if res == target:
                ans.append(temp)
            return

        st = ""
        curr = 0
        for j in range(index, len(s)):
            if j > index and s[index] == '0':
                break
            st += s[j]
            curr = curr * 10 + int(s[j])
            if index == 0:
                self.dfs(j+1, s, target, ans, temp + st, curr, curr)
            else:
                self.dfs(j+1, s, target, ans, temp + "+" + st, curr, res+curr)
                self.dfs(j+1, s, target, ans, temp + "-" + st, -curr, res-curr)
                self.dfs(j+1, s, target, ans, temp + "*" + st, prev*curr, res-prev+prev*curr)

    def addOperators(self, num: str, target: int) -> List[str]:
        ans = []
        temp = ""
        prev = 0
        self.dfs(0, num, target, ans, temp, prev, 0)
        return ans

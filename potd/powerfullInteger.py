'''
https://practice.geeksforgeeks.org/problems/d894706c496da5c5a4f45b0360c7f4164c516f83/1
'''

from typing import List


class Solution:

    def powerfullInteger(self, n: int, intervals: List[List[int]],
                         k: int) -> int:
        ints = []
        for start, end in intervals:
            ints.extend([(start, -1), (end, 1)])
        ints.sort()

        n, ans = 0, -1
        for time, typ in ints:
            if typ == -1:
                n += 1
            else:
                if n >= k:
                    ans = max(ans, time)
                n -= 1
        return ans


'''
TLE at 1024
'''

from typing import List


class Solution:

    def powerfullInteger(self, n: int, intervals: List[List[int]],
                         k: int) -> int:
        m = 0
        for i in intervals:
            m = max(m, i[1])
        l = [0] * (m + 1)
        ans = []
        mk = 0
        for i in intervals:
            for j in range(i[0] - 1, i[1]):
                l[j] += 1
                mk = max(mk, l[j])
        if (mk < k):
            return -1
        else:
            for i in range(len(l)):
                if (l[i] >= k):
                    ans.append(i + 1)
            return max(ans)
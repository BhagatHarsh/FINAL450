'''
https://practice.geeksforgeeks.org/problems/d385b9d635b7b10eef6bf365b84922aaeec9eb98/1
'''


class Solution:

    def stringMirror(self, str: str) -> str:

        i = 1
        while i < len(str):
            if str[i] > str[i - 1]:
                break
            i += 1
        s = str[:i]
        if len(s) > 1 and s[0] == s[1]:
            return s[:2]

        return s + s[::-1]

# https://practice.geeksforgeeks.org/problems/13eb74f1c80bc67d526a69b8276f6cad1b8c3401/1

#POTD Feb 25 2023
#User function Template for python3


class Solution:

    def checkCompressed(self, S, T):
        newT = ""
        cerr = ""
        for i in range(len(T)):
            if (48 <= ord(T[i]) <= 58):
                cerr += T[i]
            elif (cerr != ""):
                newT += ("_" * int(cerr))
                newT += T[i]
                cerr = ""
            else:
                newT += T[i]
        if (cerr != ""):
            newT += ("_" * int(cerr))
            cerr = ""

        # print(newT, len(S), len(newT))
        # print(newT[0:20])
        # print(S[0:20])

        if (len(S) != len(newT)):
            return 0

        for i in range(len(S)):
            if (newT[i] != "_" and newT[i] != S[i]):
                # print(newT[i],S[i])
                return 0
        return 1


#{
# Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        S = input()
        T = input()

        ob = Solution()
        print(ob.checkCompressed(S, T))
# } Driver Code Ends
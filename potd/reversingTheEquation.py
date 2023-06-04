'''
https://practice.geeksforgeeks.org/problems/reversing-the-equation2205/1
'''

class Solution:
    def reverseEqn(self, s):
        ops = ['+','-','/','*']
        sp = []
        tp = ""
        op = []
            if(i in ops):
                op.append(i)
                sp.append(tp)
                tp = ""
            else:
                tp+=i
        sp.append(tp)
        # print(sp)
        # print(op)
        ans = sp[-1]
        for i in reversed(range(len(op))):
            ans+=op[i]
            ans+=sp[i]
        
        return ans

#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        s = input().strip()
        ob = Solution()
        ans = ob.reverseEqn(s)
        print(ans)
# } Driver Code Ends

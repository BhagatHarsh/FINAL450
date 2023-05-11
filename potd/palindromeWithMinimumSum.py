'''
https://practice.geeksforgeeks.org/problems/32dc957908c2eb8beeeaeedf81f37df20d37c308/1
'''
class Solution:
    def asciisum(self,s,n):
        summ,n =  0,n
        for i in range(1,n):
            summ += abs(ord(s[i])-ord(s[i-1]))
        return summ

    def minimumSum(self, s : str) -> int:
        # code here
        s =list(s)
        n=len(s)
        i=0
        while i<(n//2):
            if s[i]=='?' and s[n-i-1]=='?':
                if (i > 0):
                    s[i], s[n-i-1] = s[i-1], s[i-1]
                else:
                    ele, idx, idx2 = '',1,n-2
                    while idx < idx2:
                        if s[idx] != '?':
                            ele = s[idx]
                            break
                        elif s[idx2] != '?':
                            ele = s[idx2]
                            break
                        idx += 1
                        idx2 -= 1
                    if ele:
                        s[i], s[n-i-1] = ele,ele
                    else:
                        s[i], s[n-i-1] = 'a','a'
            elif (s[i]!='?') and (s[n-i-1]!='?') and (s[i]!=s[n-i-1]):
                return -1
            elif (s[i]=='?' and s[n-i-1]!='?') or (s[i]!='?' and s[n-i-1]=='?'):
                if s[i]=='?':
                    s[i]=s[n-i-1]
                else:
                    s[n-i-1]=s[i]
            i+=1
        return self.asciisum(s,n) 

#{ 
 # Driver Code Starts
if __name__=="__main__":
    t = int(input())
    for _ in range(t):
        
        s = (input())
        
        obj = Solution()
        res = obj.minimumSum(s)
        
        print(res)
        

# } Driver Code Ends

# my failed attempt WA tc 14

# class Solution:
#     def min_ascii_sum(self, s):
#         n = len(s)
#         total_sum = 0
#         for i in range(n-1):
#             total_sum += abs(ord(s[i+1]) - ord(s[i]))
#         return total_sum
        
#     def minimumSum(self, S : str) -> int:
#         S = list(S)
#         n = len(S)
#         valid_char = ''
#         for i in range(n):
#             if(S[i] != '?'):
#                 valid_char = S[i]
#                 break
#         if(valid_char == ''):
#             return 0
#         for i in range(n // 2):
#             if S[i] == '?' and S[n - i - 1] != '?':
#                 S[i] = S[n - i - 1]
#             elif S[i] != '?' and S[n - i - 1] == '?':
#                 S[n - i - 1] = S[i]
#             elif S[i] == '?' and S[n - i - 1] == '?':
#                 left_char = next((S[j] for j in range(i-1, -1, -1) if S[j] != '?'), None)
#                 right_char = next((S[j] for j in range(n-i, n) if S[j] != '?'), None)
#                 if left_char is None and right_char is None:
#                     S[i] = valid_char
#                     S[n-i-1] = valid_char
#                 else:
#                     if left_char is None:
#                         left_char = right_char
#                     elif right_char is None:
#                         right_char = left_char
#                     mean_ascii = (ord(left_char) + ord(right_char)) // 2
#                     closest_char = chr(mean_ascii) if abs(mean_ascii - ord(left_char)) <= abs(mean_ascii - ord(right_char)) else chr(mean_ascii+1)
#                     S[i] = closest_char
#                     S[n-i-1] = closest_char
#         new_S = ''.join(S)
#         if new_S != new_S[::-1]:
#             return -1
#         else:
#             return self.min_ascii_sum(new_S)
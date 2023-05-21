'''
reverse a string
using a recursive function

'''

def reverse(s , i):
    if i == 0:
        return s[i]
    else:
        return s[i] + reverse(s, i-1)
    
print(reverse('hello', 4))



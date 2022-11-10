'''
program to find the maximum and minimum element in an array

'''

l = list(map(int, input("Enter the array elements: ").split()))  # input array
n = len(l)
mini = l[-1]
maxi = l[0]

i = 0
j = n-1

while(i < j):
    maxi = max(maxi, l[i], l[j])
    mini = min(mini, l[i], l[j])
    
    i+=1
    j-=1

print("Minimum element in the array is: ", mini)
print("Maximum element in the array is: ", maxi)

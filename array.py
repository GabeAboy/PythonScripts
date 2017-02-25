#python program simple array adding elements inside



# while loop that pops off all from array and stops when empty

import sys


n = int(raw_input().strip())#3
arr = map(int,raw_input().strip().split(' '))# 123
#len(arr) is redundant in this situation because we have n
count = len(arr) # 4
old = 0
while (count != 0):
    new = arr.pop()
    old+=new
    count -=1
print old




'''
import sys
n = int(raw_input().strip())#3
arr = map(int,raw_input().strip().split(' '))# 123

for i in range(n):#3  times
    new = arr.pop()
    new += arr.pop()
    print new
            #arr 1  + arr 2 = 1 + 2 = 3
            #then i becomes 2 arr 2 + arr 3 = 5
    #arg = arr[i] +arr[i]+1'''
    

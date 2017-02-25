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



raw_input()
a = map(int,raw_input().strip().split(" "))#this alone makes a list
print a # difference of output
'''[1,2] and (1,2)'''
a = tuple(a)#converts to a tuple
print a
print hash(a)
#print hash(tuple(map(int, raw_input().strip().split(" "))))






##user_input = (raw_input())
##hashable_input = user_input.replace(' ',',')
##T2 = [map(int, x) for x in hashable_input]
##print hash(T2)
##
##hashed = hash(hashable_input)
##print hashed

##a = '1 2 3 4 5'
##print a.replace(' ',',')
##print hash(a)


'''str = '1 2 3 4 5';
str_tuple= str.split()
print hash(str_tuple)
Doesnt work because lists are unhashable
output = '1','2','3','4','5'
'''

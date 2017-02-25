print 'please enter a number in range'
n = int(raw_input())
if 0<n<20:
    i=0
    
    while i<n:
        ans = i**2
        print ans
        
        i+=1

else:
    print'wrong'
    

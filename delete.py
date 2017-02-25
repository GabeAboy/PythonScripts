def main():

#list_dict is for the user input values
 #dick is for the traveresed input for print
    list_dict = []
    dick = []
    
    N = int(raw_input())
    
#this loop asks the user to input the number
    #of times he specified earlier
    #enters the values into the first
    #input dictionary
    for i in range (N):
        user = raw_input('enter: ')
        list_dict.insert(i,user)
    list_dict.reverse()#Fixes output error
    print len(list_dict)

    
    i = 0
    while i<=N:#len(list_dict)!=0:

        for i in xrange (len(list_dict)):
            print 'before pop'
            print (list_dict)

            queue = list_dict.pop()
            print 'before split'
            print queue
            operation = queue[0:3]
            print queue
            print list_dict
            print operation

            if operation == 'ins':
                print 'ifloop'
                print operation
                

            else:
                print ' reject'

    #print dick[0]

            
    i+=1
    
main()

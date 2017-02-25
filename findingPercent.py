#How many people?
n = int(raw_input())
#Create dictionary
mydict = {}
#for loop iterating the amount of people for
#inputing 
for line in range(n):
    #for each space
    info = raw_input().split(" ")
    #map(function,iterable,..) function
    #Apply function to every item of iterable and
    #return a list of the results
    score = map(float, info[1:])
    
    mydict[info[0]] = sum(score) / float(len(score))
#prints only two decimal spaces
    
print "%.2f" % round(mydict[raw_input()],2)

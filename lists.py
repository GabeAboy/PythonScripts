
#ask user for how many inputs
T = int(raw_input())
#creat dictionary
L = []
#loop that reads input in range
for i in range(T):
    #ask 
    user = raw_input().strip().split(" ")
    #if else for each argument
    if user[0] =="append":
        L.append(int(user[1]))
    elif user[0] == "insert":
        L.insert(int(user[1]),int(user[2]))
    elif user[0] == "remove":
        L.remove(int(user[1]))
    elif user[0] == "pop":
        L.pop()
    elif user[0] == "sort":
        L.sort()
    elif user[0] == "reverse":
        L.reverse()
    elif user[0] == "print":
        print L

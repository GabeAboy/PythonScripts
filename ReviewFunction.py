def shut_down(s):
    error= "Shutting down"
    abort='Shutdown aborted'
    sorry='Sorry'
    if s =="yes":
    
        return error
    elif s =="no":
        return abort
    else:
        return sorry
        
word = raw_input('yes or no')
s= word.lower()

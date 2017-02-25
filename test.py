'''number = raw_input("Enter number:  ")


def cube(number):
    answer = number**3
    return(answer)

def by_three(answer):
    if answer % 3 == 0:
        return cube(answer)
    else:
        return(False)
cube(number)'''
def cube(number):
    return number**3
def by_three(number):
    if number%3==0:
        cube(number)
        return cube(number)
        
        
    else:
        return False


by_three(3)

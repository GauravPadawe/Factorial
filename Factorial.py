def factorial(n):             # Defining a procedure factorial
    i = 1                     # Creating reference variable "i" having value 1
    a = range(n, 1, -1)       # Setting range by passing value of n which will go till 1 by -1 unit
    for x in a:               # Getting individual values of a
        i = i * x             # i will get updated every time in for loop with new value of a
    return i
    
print factorial(10)

# CODED BY - GAURAV PADAWE

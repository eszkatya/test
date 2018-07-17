#Create a function isDivisible(n, x, y) that checks if a number n is divisible by two numbers x AND y. 
#All inputs are positive, non-zero digits.

def is_divisible(n,x,y):
    if n % x == 0 and n % y == 0:
        return True
    else:
        return False
"""def is_divisible(n,x,y):
    return n % x == 0 and n % y == 0
    
    itt nem volt nagy változatosság, vagy ehhez nagyon hasonló kódok..vagy lambdás megoldások

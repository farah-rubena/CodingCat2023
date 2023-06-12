'''Given 2 int values, return True if one is negative and one is positive. 
Except if the parameter "negative" is True, then return True only if both are negative.
'''

def posneg(a,b,negative):

    if negative:
        if a < 0 and b < 0:
            return True
    elif (a > 0 and b < 0) or (a < 0 and b > 0):
        return True
    else:
        return False
    

print(posneg(1, -1, False))
print(posneg(-1, 1, False))
print(posneg(-4, -5, True))



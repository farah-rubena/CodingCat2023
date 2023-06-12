'''The parameter weekday is True if it is a weekday, and the parameter vacation is True if we are on vacation. 
We sleep in if it is not a weekday or we're on vacation. Return True if we sleep in.

'''

def sleepin(weekday, vacation):

    if not weekday or vacation:
        return True
    else:
        return False

print(sleepin(False, False))
print(sleepin(True, False))
print(sleepin(False, True))




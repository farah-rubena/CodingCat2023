'''Given 2 ints, a and b, return True if one if them is 10 or if their sum is 10.

'''

def makes_10(a,b):

    if a == 10 or b == 10 or (a+b) == 10:
        return True
    return False

print(makes_10(9, 10))
print(makes_10(9, 9))
print(makes_10(1, 9))


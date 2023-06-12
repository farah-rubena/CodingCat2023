'''Given two int values, return their sum. Unless the two values are the same, then return double their sum.

'''

def sumdouble(a, b):

    if a == b:
        return (a+b) * 2
    else:
        return a + b

print(sumdouble(1, 2))
print(sumdouble(3, 2))
print(sumdouble(2, 2))
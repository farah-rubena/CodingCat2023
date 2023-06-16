'''Given 2 ints, a and b, return their sum. However, sums in the range 10..19 inclusive, are forbidden, 
so in that case just return 20.
'''

def sortasum(a,b):

    sum = a + b

    if sum in range(10, 20):
        return 20
    else:
        return sum

print(sortasum(3, 4))
print(sortasum(9, 4))
print(sortasum(10, 11))


'''Given 2 arrays of ints, a and b, 
return True if they have the same first element or they have the same last element. 
Both arrays will be length 1 or more.

'''

def commonend(a,b):

    if a[0] == b[0] or a[-1] == b[-1]:
        return True
    else:
        return False

print(commonend([1, 2, 3], [7, 3]))
print(commonend([1, 2, 3], [7, 3, 2]))
print(commonend([1, 2, 3], [1, 3]))

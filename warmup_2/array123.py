'''Given an array of ints, return True if the sequence of numbers 1, 2, 3 appears in the array somewhere.

'''

def array_123(num_list):

    check = [1,2,3]

    for _ in range(len(num_list)):
        if num_list[_:_+3] == check:
            return True
    else:
        return False

print(array_123([1, 1, 2, 3, 1]))
print(array_123([1, 1, 2, 4, 1]))
print(array_123([1, 1, 2, 1, 2, 3]))

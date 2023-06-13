'''Given an array of ints, return True if one of the first 4 elements in th e array is a 9. The array length may be less than 4.

'''

def arrayfront9(num_list):

    count = 0
    for _ in range(len(num_list)):
        if _ <4 and num_list[_] == 9:
            count += 1

    return count


print(arrayfront9([1, 2, 9, 3, 4]))
print(arrayfront9([1, 2, 3, 4, 9]))
print(arrayfront9([1, 2, 3, 4, 5]))


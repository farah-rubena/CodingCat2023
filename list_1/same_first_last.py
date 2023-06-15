'''Given an array of ints, return True if the array is length 1 or more, and the first element and the last element are equal.

'''


def samefirstlast(num_list):

    if len(num_list) >= 1 and num_list[0] == num_list[-1]:
        return True
    else:
        return False
    
print(samefirstlast([1, 2, 3]))
print(samefirstlast([1, 2, 3, 1]))
print(samefirstlast([1, 2, 1]))

'''Given an array of ints, return the number of 9's in the array.

'''

#the same can be done using a for loop

def arraycount9(num_list):

    return num_list.count(9)

print(arraycount9([1, 2, 9]))
print(arraycount9([1, 9, 9]))
print(arraycount9([1, 9, 9, 3, 9]))


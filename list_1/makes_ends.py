'''Given an array of ints, return a new array length 2 containing the first and last elements from the original array. The original array will be length 1 or more.
'''

def makesends(num_list):

    return [num_list[0], num_list[-1]]

print(makesends([1, 2, 3]))
print(makesends([1, 2, 3, 4]))
print(makesends([7, 4, 6, 2]))

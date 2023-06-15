'''Given an array of ints length 3, return a new array with the elements in reverse order, so {1, 2, 3} becomes {3, 2, 1}.

'''

def reverse_3(num_list):

    return num_list[::-1]

print(reverse_3([1, 2, 3]))
print(reverse_3([5, 11, 9]))
print(reverse_3([7, 0, 0]))

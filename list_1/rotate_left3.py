''''Given an array of ints length 3, return an array with the elements "rotated left" so {1, 2, 3} yields {2, 3, 1}.

'''

def rotateleft3(num_list):

    first_num = num_list[0]
    return num_list[1:] + [first_num]

print(rotateleft3([1, 2, 3]))
print(rotateleft3([5, 11, 9]))
print(rotateleft3([7, 0, 0]))




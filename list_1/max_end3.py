'''Given an array of ints length 3, figure out which is larger, the first or last element in the array,
 and set all the other elements to be that value. Return the changed array.

'''

def maxend3(num_list):

    largest_num = 0

    for _ in num_list:
        if num_list[0] > num_list[-1]:
            largest_num = num_list[0]
        else:
            largest_num = num_list[-1]

    new_list = []
    for _ in num_list:
        _ = largest_num
        new_list.append(_)
    return new_list

print(maxend3([1, 2, 3]))
print(maxend3([11, 5, 9]))
print(maxend3([2, 11, 3]))

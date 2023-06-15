'''Given an array of ints, return True if 6 appears as either the 
first or last element in the array. The array will be length 1 or more.

'''

def firstlast6(num_list):

    if num_list[0] == 6 or num_list[-1] == 6:
        return True
    else:
        return False
    
print(firstlast6([1, 2, 6]))
print(firstlast6([6, 1, 2, 3]))
print(firstlast6([13, 6, 1, 2, 3]))


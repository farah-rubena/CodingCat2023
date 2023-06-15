'''Given an int array length 2, return True if it contains a 2 or a 3.
'''

def has23(num_list):

    if 2 in num_list or 3 in num_list:
        return True
    return False
    

print(has23([2, 5]))
print(has23([4, 3]))
print(has23([4, 5]))

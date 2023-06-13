'''Given 2 strings, a and b, return the number of the positions 
where they contain the same length 2 substring. So "xxcaazz" and "xxbaaz" yields 3, 
since the "xx", "aa", and "az" substrings appear in the same place in both strings.

'''

def stringmatch(a, b):

    #find the shorter strinf
    shortest = min(a,b)

    count = 0
    for _ in range(len(shortest)-1):
        if a[_:_+2] == b[_:_+2]:
            count += 1

    return count


print(stringmatch('xxcaazz', 'xxbaaz'))
print(stringmatch('abc', 'abc'))
print(stringmatch('abc', 'axc'))


'''Given two strings, return True if either of the strings appears at the very end of the other string, 
ignoring upper/lower case differences (in other words, the computation should not be "case sensitive").
 Note: s.lower() returns the lowercase version of a string.

'''

def endother(a,b):
    lower_a = a.lower()
    lower_b = b.lower()
    lenght_a = len(lower_a)
    lenght_b = len(lower_b)

    for _ in range(len(lower_a)):
        #print(lower_a[-lenght_b:])
        if lower_a[-lenght_b:] == lower_b:
            return True
        if lower_b[-lenght_a:] == lower_a:
            return True
    else:
        return False

print(endother('Hiabc', 'abc'))
print(endother('AbC', 'HiaBc'))
print(endother('abc', 'abXabc'))
  

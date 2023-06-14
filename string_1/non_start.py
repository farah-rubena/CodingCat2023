'''Given 2 strings, return their concatenation, except omit the first char of each. The strings will be at least length 1.

'''

def nonstart(a,b):

    return f"{a[1:] + b[1:]}"

print(nonstart('Hello', 'There'))
print(nonstart('java', 'code'))
print(nonstart('shotl', 'java'))

'''Given a non-empty string and an int n, return a new string where the char at index n has been removed.
 The value of n will be a valid index of a char in the original string (i.e. n will be in the range 0..len(str)-1 inclusive).

'''

def missingchar(text, n):

    new_str = ""

    for _ in range(len(text)    ):
        if n == _:
            continue
        else:
            new_str += (text[_])
    return new_str

print(missingchar('kitten', 1))
print(missingchar('kitten', 0))
print(missingchar('kitten', 4))

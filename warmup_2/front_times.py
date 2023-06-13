'''Given a string and a non-negative int n, we'll say that the front of the string is the first 3 chars,
 or whatever is there if the string is less than length 3. Return n copies of the front;


'''

def fronttimes(text, n):

    return text[:3] * n
    
print(fronttimes('Chocolate', 2))
print(fronttimes('Chocolate', 3))
print(fronttimes('Abc', 3))


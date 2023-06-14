'''Given a string, return a version without the first and last char, so "Hello" yields "ell". The string length will be at least 2.

'''

def withoutend(text):

    if len(text)<2:
        return text
    else:
        return text[1:-1]
    
print(withoutend('Hello'))
print(withoutend('java'))
print(withoutend('coding'))


'''Given a string, return a new string made of 3 copies of the last 2 chars of the original string. The string length will be at least 2.

'''

def extraend(text):

    if len(text) < 2:
        return text
    else:
        return text[-2:] * 3
    

print(extraend('Hello'))
print(extraend('ab'))
print(extraend('Hi'))


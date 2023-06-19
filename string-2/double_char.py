''''Given a string, return a string where for every char in the original, there are two chars.

'''

def doublechar(text):

    newtext = ""
    for _ in text:
        newtext+=_ *2 
    return newtext

print(doublechar('The'))
print(doublechar('AAbb'))
print(doublechar('Hi-There'))



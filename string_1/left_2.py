'''Given a string, return a "rotated left 2" version where the first 2 chars are moved to the end. The string length will be at least 2.

'''

def left2(text):

    return text[2:]+text[:2]

print(left2('Hello'))
print(left2('java'))
print(left2('Hi'))
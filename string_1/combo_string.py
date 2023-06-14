'''Given 2 strings, a and b, return a string of the form short+long+short, 
with the shorter string on the outside and the longer string on the inside. 
The strings will not be the same length, but they may be empty (length 0).

'''

def combostring(a,b):

    if len(a) < len(b):
        return f"{a}{b}{a}"
    else:
        return f"{b}{a}{b}"

print(combostring('Hello', 'hi'))
print(combostring('hi', 'Hello'))
print(combostring('aaa', 'b'))

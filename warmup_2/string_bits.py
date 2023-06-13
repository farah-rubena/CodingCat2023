'''Given a string, return a new string made of every other char starting with the first, so "Hello" yields "Hlo".

'''

def stringbits(text):

    new_str = ""
    for _ in range(len(text)):
        if _%2 == 0:
            new_str += text[_]
        else:
            continue
                
    return new_str

print(stringbits('Hello'))
print(stringbits('Hi'))
print(stringbits('Heeololeo'))
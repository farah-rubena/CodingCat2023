'''Given a string of even length, return the first half. So the string "WooHoo" yields "Woo".

'''
def firsthalf(text):

    half = int(len(text)/2)
    #print(half)
    return text[:half]

print(firsthalf('WooHoo'))
print(firsthalf('HelloThere'))
print(firsthalf('abcdef'))

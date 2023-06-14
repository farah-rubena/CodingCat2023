'''Given an "out" string length 4, such as "<<>>", and a word, 
return a new string where the word is in the middle of the out string, e.g. "<<word>>".

'''

def makeoutword(out, text):

    return f"{out[:2]}{text}{out[2:]}"

print(makeoutword('<<>>', 'Yay'))
print(makeoutword('<<>>', 'WooHoo'))
print(makeoutword('[[]]', 'word'))
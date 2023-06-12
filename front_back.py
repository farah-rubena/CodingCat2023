'''Given a string, return a new string where the first and last chars have been exchanged.

'''

def frontback(text):
    
    if len(text) >= 1:
        return text[-1] + text[1:-1] + text[0]
    else:
        return text

print(frontback('code'))
print(frontback('a'))
print(frontback('ab'))

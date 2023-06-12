'''Given a string, return a new string where "not " has been added to the front.
However, if the string already begins with "not", return the string unchanged.

'''

def notstring(text):

    if text[:3] == "not":
        return text
    else:
        return "not " + text
    
print(notstring('candy'))
print(notstring('x'))
print(notstring('not bad'))



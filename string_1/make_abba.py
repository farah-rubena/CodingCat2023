'''Given two strings, a and b, return the result of putting them together in the order abba, e.g. "Hi" and "Bye" returns "HiByeByeHi".

'''

def makeabba(a,b):

    return f"{a}{b}{b}{a}"

print(makeabba('Hi', 'Bye'))
print(makeabba('Yo', 'Alice'))
print(makeabba('What', 'Up'))

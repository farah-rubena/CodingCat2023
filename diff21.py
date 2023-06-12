'''Given an int n, return the absolute difference between n and 21, except return double the absolute difference if n is over 21.
* we can use the in-built funvtion abs()
The absolute difference is a mathematical concept that measures the numerical distance between two values, without considering their direction or sign.
It is the positive value of the difference between two numbers.
'''

def diff_21(n):

    if n > 21:
        return abs(n-21)*2
    else:
         return abs(n-21)
    
print(diff_21(19))
print(diff_21(10))
print(diff_21(21))






'''We have a loud talking parrot. The "hour" parameter is the current hour time in the range 0..23. 
We are in trouble if the parrot is talking and the hour is before 7 or after 20. Return True if we are in trouble.

'''

def parrottrouble(talking, hour):

    if talking and hour < 7 or hour > 20:
        return True 
    else:
        return False

print(parrottrouble(True, 6))
print(parrottrouble(True, 7))
print(parrottrouble(False, 6))



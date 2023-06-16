'''The squirrels in Palo Alto spend most of the day playing.
 In particular, they play if the temperature is between 60 and 90 (inclusive). 
 Unless it is summer, then the upper limit is 100 instead of 90. 
 Given an int temperature and a boolean is_summer, return True if the squirrels play and False otherwise.

'''

def squirrelplay(temperature, is_summer):

    if is_summer:
        return temperature >=60 and temperature <=100
    else:
        return temperature >=60 and temperature<=90
        
print(squirrelplay(70, False))
print(squirrelplay(95, False))
print(squirrelplay(95, True))


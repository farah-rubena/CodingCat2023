'''We want to make a row of bricks that is goal inches long. 
We have a number of small bricks (1 inch each) and big bricks (5 inches each).
 Return True if it is possible to make the goal by choosing from the given bricks.
   This is a little harder than it looks and can be done without any loops.

'''
    
def makebricks(small, big, goal):

    return (goal%5)<=small and (goal-(big*5))<=small

print(makebricks(3, 1, 8))
print(makebricks(3, 1, 9))
print(makebricks(3, 2, 10))


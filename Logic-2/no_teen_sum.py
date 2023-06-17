'''Given 3 int values, a b c, return their sum. 
However, if any of the values is a teen -- in the range 13..19 inclusive -- 
then that value counts as 0, except 15 and 16 do not count as a teens. 
Write a separate helper "def fix_teen(n):"that takes in an int value and returns that value fixed for the teen rule. 
In this way, you avoid repeating the teen code 3 times (i.e. "decomposition"). 
Define the helper below and at the same indent level as the main no_teen_sum().

'''

def fix_teen(num):
    
    if num in [13,14,17,18,19]:
        return 0
    return num
        
#print(fix_teen(13))

def noteensum(a,b,c):

    return fix_teen(a) + fix_teen(b) + fix_teen(c)

print(noteensum(1, 2, 3))
print(noteensum(2, 13, 1))
print(noteensum(2, 1, 14))








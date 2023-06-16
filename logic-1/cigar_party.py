'''When squirrels get together for a party, they like to have cigars.
 A squirrel party is successful when the number of cigars is between 40 and 60, inclusive. 
 Unless it is the weekend, in which case there is no upper bound on the number of cigars. 
 Return True if the party with the given values is successful, or False otherwise.

'''

def cigarparty(cigars, weekend):

    if weekend and cigars >= 40:
        return True
    elif not weekend and cigars >= 40 and cigars <=60:
        return True
    else:
        return False
    
print(cigarparty(30, False))
print(cigarparty(50, False))
print(cigarparty(70, True))


'''Return True if the string "cat" and "dog" appear the same number of times in the given string.

'''

def catdog(text):

    cat_count = 0
    dog_count = 0
    for _ in range(len(text)-1):
        if text[_:_+3] == "dog":
            dog_count+=1
        if text[_:_+3] == "cat":
            cat_count += 1
    if dog_count == cat_count:
        return True
    else:
        return False

print(catdog('catdog'))
print(catdog('catcat'))
print(catdog('1cat1cadodog')) 


'''Return the number of times that the string "hi" appears anywhere in the given string.

'''

def counthi(text):

    count = 0
    for _ in range(len(text)-1):
        
        if text[_:_+2] == "hi" :
            count += 1
    return count

print(counthi('abc hi ho'))
print(counthi('ABChi hi'))
print(counthi('hihi'))


        
        
        
        



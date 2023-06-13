'''Given a string, return the count of the number of times that a 
substring length 2 appears in the string and also as the last 2 chars of the string,
 so "hixxxhi" yields 1 (we won't count the end substring).

'''

def last2(text):

    if len(text) < 2:
        return 0
    
    #get last 2 characters
    last_two = text[-2:]
    count = 0

    #exclude last two characters
    for i in range(len(text)-2):
        if text[i:i+1] == last_two:
            count += 1

    return count
        

print(last2('hixxhi'))
print(last2('xaxxaxaxx'))
print(last2('axxxaaxx'))

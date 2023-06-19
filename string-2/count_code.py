'''Return the number of times that the string "code" appears anywhere in the given string,
 except we'll accept any letter for the 'd', so "cope" and "cooe" count.

'''
#Note : by subtracting 3 from the length of the string we ensure that the loop iterates only till the 3-rd last character 
def countcode(text):

    count = 0
    for _ in range(len(text)-1):
        if text[_:_+2] == "co" and text[_+3] == "e":
            count += 1
    return count

print(countcode('aaacodebbb'))
print(countcode('codexxcode'))
print(countcode('cozexxcope'))



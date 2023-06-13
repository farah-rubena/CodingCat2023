'''Given a non-empty string like "Code" return a string like "CCoCodCode".

'''

def stringsplosion(text):


    new_text = ""
    for _ in range(len(text)+1):
        new_text += text[:_]
    return new_text


print(stringsplosion('Code'))
print(stringsplosion('abc'))
print(stringsplosion('ab'))




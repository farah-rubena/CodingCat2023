''''The web is built with HTML strings like "<i>Yay</i>" which draws Yay as italic text. 
In this example, the "i" tag makes <i> and </i> which surround the word "Yay". 
Given tag and word strings, create the HTML string with tags around the word, e.g. "<i>Yay</i>".

'''

def maketags(tags, text):

    return f"<{tags}>{text}</{tags}>"

print(maketags('i', 'Yay'))
print(maketags('i', 'Hello'))
print(maketags('cite', 'Yay'))

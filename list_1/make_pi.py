'''Return an int array length 3 containing the first 3 digits of pi, {3, 1, 4}.'''

def makepi():

    pi = "3.14159"
    new_list = []

    for _ in range(len(pi)):
        if _ <= 3:
            if pi[_] == ".":
                continue
            else:
                new_list.append(pi[_])

    return new_list

print(makepi())

def findvalue(mydict, val):
    keylist = []
    for key in mydict:
        if val in mydict[key]:
            keylist.append(key)
    return keylist


if __name__ == "__main__":
    dictionary = {"Student": ["Stiv", "Steve"], "Smart": "", "Bully": ""}
    user_input = input("Enter a value of a key(s): ")
    print(findvalue(dictionary, user_input))

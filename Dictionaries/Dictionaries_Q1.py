def removekeys(mydict, keylist):
    for keys in keylist:
        if keys in mydict:
            mydict.pop(keys)
    return mydict


if __name__ == "__main__":
    dictionary = {"breed": "poodle", "gender": "male", "age": 20, "colour": "brown"}
    key_ls = ["gender", "breed", "age"]
    print(removekeys(dictionary, key_ls))

import string


def char_freq(str):
    for i in str.upper():
        for j in string.ascii_uppercase:
            if j.count(i) == 0:
                pass
            else:
                print(j, ":", j.count(i))



if __name__ == "__main__":
    text = input("Enter word: ")
    char_freq(text)


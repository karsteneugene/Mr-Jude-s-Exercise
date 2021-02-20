import string


def check_pangram(temp_text):
    for i in string.ascii_lowercase:
        if i not in temp_text.lower():
            return False
    return True


if __name__ == "__main__":
    text = input("Enter sentence to check if it is a pangram: ")
    print("")
    if check_pangram(text) is True:
        print("Sentence is a pangram")
    else:
        print("Sentence is not a pangram")

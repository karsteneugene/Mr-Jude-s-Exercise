import re


def hapax(book):
    # Opens the file
    file = open(book, "r", encoding="utf8")
    # Automatically creates a list that only contains alphanumeric characters
    word_list = re.findall('\w+', file.read().lower())
    freq = {}
    # for loop checks if each word in the list is added to the dictionary. If not, adds the word as a key and set 1 as
    # its count. If it is added before, adds count by 1
    for word in word_list:
        if word not in freq:
            freq[word] = 1
        elif word in freq:
            freq[word] += 1
    # for loop checks for all the words in the dictionary that has a count of 1. If it only has 1 count, then its a
    # hapax
    for word in freq:
        if freq[word] == 1:
            # displays all the hapax
            print(word)
    file.close()


if __name__ == "__main__":
    print("Here are the hapaxes for this text:")
    hapax("Little Helpers.txt")

def filter_long_words(lwords, n):
    new_list = []
    for i in lwords:
        if len(i) > n:
            new_list.append(i)
        else:
            pass
    return new_list


if __name__ == "__main__":
    word_lst = list(input("Enter a list of long words: ").split(","))
    x = int(input("Enter minimum length of desired words: "))
    print("")
    print("Words with more than", x, "letters:", filter_long_words(word_lst, x))

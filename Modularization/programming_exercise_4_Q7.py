def words_2_int(lst):
    num_lst = []
    for i in lst:
        num_lst.append(len(i))
    return num_lst


if __name__ == "__main__":
    word_lst = list(input("Enter words: ").split(","))
    print(words_2_int(word_lst))

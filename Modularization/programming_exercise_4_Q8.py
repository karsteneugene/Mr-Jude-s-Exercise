def find_longest_word(lwords):
    num_lst = []
    for i in lwords:
        num_lst.append(len(i))
    return max(num_lst)


if __name__ == "__main__":
    user_lst = list(input("Enter a list of long words: ").split(","))
    print("")
    print("Longest word length:", find_longest_word(user_lst))

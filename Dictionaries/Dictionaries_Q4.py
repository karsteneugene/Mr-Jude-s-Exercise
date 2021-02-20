def wordfrequencies(mylist):
    freq_dict = {}
    for word in mylist:
        if word not in freq_dict:
            freq_dict[word] = 1
        elif word in freq_dict:
            freq_dict[word] += 1
    return freq_dict


if __name__ == "__main__":
    word_ls = ["hello", "hello", "hello", "this", "is", "a", "test", "test"]
    print(wordfrequencies(word_ls))

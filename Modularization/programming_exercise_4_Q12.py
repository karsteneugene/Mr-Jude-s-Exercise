def make_forms(verb):
    if verb[-1] == "y":
        new = verb[:-1].split()
        new = new[0] + "ies"
    elif verb[-1] == "o":
        new = verb + "es"
    elif verb[-1] == "s":
        new = verb + "es"
    elif verb[-1] == "x":
        new = verb + "es"
    elif verb[-1] == "z":
        new = verb + "es"
    elif verb[-2::] == "ch":
        new = verb + "es"
    elif verb[-2::] == "sh":
        new = verb + "es"
    else:
        new = verb + "s"
    return new


if __name__ == "__main__":
    word = input("Enter word: ")
    print("")
    print("Third person singular form:", make_forms(word))

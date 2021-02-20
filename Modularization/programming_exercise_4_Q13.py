def make_forming(verb):
    new = ""
    consonant_lst = ["b", "c", "d", "f", "g", "h", "j", "k", "l", "m", "n", "p", "q", "r", "s", "t", "v", "w", "x", "y",
                     "z"]
    vowel_lst = ["a", "e", "i", "o", "u"]
    if verb == "be":
        new = verb + "ing"
    elif verb[-2::] == "ee":
        new = verb + "ing"
    elif verb[-2::] == "ie":
        new = verb[:-2].split()
        new = new[0] + "ying"
    elif verb[-1] == "e":
        new = verb[:-1].split()
        new = new[0] + "ing"
    elif verb[-1] in consonant_lst:
        if verb[:-2] in consonant_lst:
            if verb[-2:-1] in vowel_lst:
                new = verb + str(verb[-1]) + "ing"
    else:
        new = verb + "ing"
    return new


if __name__ == "__main__":
    word = input("Enter verb: ")
    print("")
    print("Present participle:", make_forming(word))
